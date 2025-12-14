import numpy as np
import matplotlib.pyplot as plt

def P_vdw_reduced(v, Tr):
    return 8*Tr/(3*v - 1) - 3/(v*v) ##reduced variable 이용한 VDW EOS 정의

####### Bisection Method 정의 ############################################
#(ChatGPT에게 Bisection Method을 이용한 1차원 근 탐색 알고리즘의 구현 방법을 물어보았음.)
def bisection_root(func, a, b, tol=1e-12, maxit=200):
    """[a,b]에서 func의 부호가 바뀔 때(func(a)*func(b)<0) 근을 이분법으로 찾음"""
    fa, fb = func(a), func(b)
    if fa == 0.0: 
        return a
    if fb == 0.0:
        return b
    if fa * fb > 0:
        raise ValueError("Bisection needs a sign change on [a,b].")

    for _ in range(maxit):
        m = 0.5*(a+b)
        fm = func(m)
        if abs(fm) < tol or 0.5*(b-a) < tol:
            return m
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5*(a+b)

#(ChatGPT에게 VDW EOS에서 P(v)=P_Level의 교점들을 
# 수치적으로 찾기 위한 알고리즘의 구현 방법을 물어보았음.)
def find_intersections_v(Tr, P_level, vmin=1/3 + 1e-3, vmax=20.0, nscan=60000):
    """
    P_vdw_reduced(v,Tr) = P_level 의 해 v들을 찾는다.
    방법: v를 촘촘히 스캔해서 부호가 바뀌는 구간을 찾고,
          각 구간에서 bisection으로 근을 정밀하게 구함.
    반환: roots (오름차순 리스트)
    """
    vgrid = np.linspace(vmin, vmax, nscan)
    g = P_vdw_reduced(vgrid, Tr) - P_level

    roots = []
    for i in range(len(vgrid) - 1):
        gi, gj = g[i], g[i+1]

        # NaN 방지
        if np.isnan(gi) or np.isnan(gj):
            continue

        # 정확히 0이면 근
        if gi == 0.0:
            roots.append(vgrid[i])
        # 부호 변화면 bracket -> bisection
        elif gi * gj < 0.0:
            a, b = vgrid[i], vgrid[i+1]
            root = bisection_root(lambda v: P_vdw_reduced(v, Tr) - P_level, a, b)
            roots.append(root)

    # 중복 근 병합(스캔이 촘촘하면 거의 같은 값이 여러 번 잡힐 수 있음)
    roots = np.array(sorted(roots))
    if len(roots) == 0:
        return []

    merged = [roots[0]]
    for r in roots[1:]:
        if abs(r - merged[-1]) > 1e-6:   # 병합 기준
            merged.append(r)

    return merged


#######################################################################

###### equal area fn 정의 ##################에 필요한 simpson공식 까지
#(ChatGPT에게 Maxwell Construction에서 면적 계산을 수행하기 위한 적분법의 구현 방법을 물어보았음.)

def simpson_integral(f, a, b, N=4000):
    if N % 2 == 1:
        N += 1
    x = np.linspace(a, b, N+1)
    y = f(x)
    h = (b-a)/N
    return (h/3)*(y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]))

#(ChatGPT에게 Maxwell의 equal-area 조건을 함수 F(P)=0 형태로 구현하는 방법을 물어보았음.)
def F_equal_area(Tr, P_level, vmin=1/3+1e-3, vmax=20.0, nscan=60000):
    roots = find_intersections_v(Tr, P_level, vmin=vmin, vmax=vmax, nscan=nscan)

    if len(roots) < 2:
        return np.nan, (None, None)

    v_l = roots[0]
    v_g = roots[-1]

    integrand = lambda v: P_vdw_reduced(v, Tr) - P_level
    F = simpson_integral(integrand, v_l, v_g, N=4000)

    return F, (v_l, v_g)


##################################################################

Tr = 0.95 #열통교과서 prob 5.52 참고

# 1) 충분히 촘촘한 vgrid 생성 (분모가 0이 되는 1/3 근처는 피하기)
vgrid = np.linspace(1/3 + 1e-3, 20.0, 400000)
Pgrid = P_vdw_reduced(vgrid, Tr)

# 2) 국소 극값(=spinodal pressure)을 수치 미분으로 찾기
dP = np.gradient(Pgrid, vgrid)

# 부호 변화 : + -> - (극댓값), - -> + (극솟값)
imax = np.where((dP[:-1] > 0) & (dP[1:] <= 0))[0] #극대
imin = np.where((dP[:-1] < 0) & (dP[1:] >= 0))[0] #극소

print("extremum counts:", len(imax), len(imin)) #극값 개수

# 3) 극댓값, 극솟값 좌표 출력
i_max = imax[0]
i_min = imin[0]

v_max, P_max = vgrid[i_max], Pgrid[i_max]
v_min, P_min = vgrid[i_min], Pgrid[i_min]

print(f"spinodal max: v={v_max:.6f}, P={P_max:.6f}") # 극대
print(f"spinodal min: v={v_min:.6f}, P={P_min:.6f}") # 극소

# 4) Tr = 0.95에서의 isothermal한 VDW EOS 곡선 확인하기. 극대극소 추가함.
plt.figure()
plt.plot(vgrid, Pgrid)
plt.axhline(P_max, linestyle="--")
plt.axhline(P_min, linestyle="--")
plt.xlim(0.3, 10)
plt.ylim(-0.5, 2.0)
plt.xlabel("v_r"); plt.ylabel("P_r")
plt.title(f"Reduced VDW Isotherm (T_r={Tr}) with spinodal P_min/P_max")
plt.grid(alpha=0.3)
plt.show()
## 여기까지: reduced variable Tr = 0.95에서의 반데발스 EOS을 그래프로 그려본 것이고, 
## 이때의 극대와 극소 v,p좌표를 찾은 것


#########################이제 Bisection method도입할 차례####################
# P는 무조건 P_min과 P_max 사이에서 찍어야 함.
Ptest = 0.5*(P_min + P_max) # Bisection Method 적용하여 극값의 절반으로 test해봄.


roots = find_intersections_v(Tr, Ptest, vmin=1/3+1e-3, vmax=20.0, nscan=60000)
print("\n\nPtest:", Ptest)
print("number of roots:", len(roots))
print("roots:", roots)
## P(v;Tr) = P의 해가 3개 존재함을 확인.
# 이는 van der Waals 등온선이 기계적 불안정 구간을 포함하는 S자 형태임을 수치적으로 확인.
# Maxwell construction이 적용될 수 있는 조건(액체상·기체상 공존 부피의 존재)을 만족.

F, (vl, vg) = F_equal_area(Tr, Ptest, vmin=1/3+1e-3, vmax=20.0)
print("\n\nF(Ptest) =", F, "\nvl", vl, "\nvg =", vg) 
## F(Ptest) 값이 양수가 나오므로 하한으로 설정. 
## 그리고 이제 F(P) < 0인 것도 찾아서 좁혀 나가야 함.

eps = 1e-4

P_right = P_max - eps #F(P_right의 좌극한)정도면 < 0 일 것이니 상한으로 설정.

F_Ptest,  _ = F_equal_area(Tr, Ptest,  vmin=1/3+1e-3, vmax=20.0, nscan=60000)
F_right, _ = F_equal_area(Tr, P_right, vmin=1/3+1e-3, vmax=20.0, nscan=60000)

print("\n\nP_right = ", P_right, "\nF_right = ", F_right)
print("\nproduct =", F_Ptest*F_right) ## product 음수 나옴 -> Bisection 범위 잘 설정함.

##### 이제 Bisection Method으로 P_eq 찾기 위해 함수의 정의해야 함.
# (ChatGPT에게 Maxwell equal-area 조건 F(P)=0을 만족하는
#  공존 압력을 Bisection Method으로 찾는 방법을 물어보았음.)

def bisection_Peq(Tr, P_L, P_R, tol=1e-8, maxit=60):
    F_L, _ = F_equal_area(Tr, P_L, vmin=1/3+1e-3, vmax=20.0, nscan=60000)
    F_R, _ = F_equal_area(Tr, P_R, vmin=1/3+1e-3, vmax=20.0, nscan=60000)

    if np.isnan(F_L) or np.isnan(F_R) or F_L*F_R > 0:
        raise ValueError("Need F(P_L) and F(P_R) to have opposite signs.")

    for _ in range(maxit):
        P_M = 0.5*(P_L + P_R)
        F_M, (v_l, v_g) = F_equal_area(Tr, P_M, vmin=1/3+1e-3, vmax=20.0, nscan=60000)

        if abs(F_M) < tol or 0.5*(P_R - P_L) < tol:
            return P_M, v_l, v_g, F_M

        if F_L*F_M < 0:
            P_R, F_R = P_M, F_M
        else:
            P_L, F_L = P_M, F_M

    P_M = 0.5*(P_L + P_R) ##범위를 절반으로 줄임 -> Bisection Method!
    F_M, (v_l, v_g) = F_equal_area(Tr, P_M, vmin=1/3+1e-3, vmax=20.0, nscan=60000)
    return P_M, v_l, v_g, F_M

## bisection_Peq(...)를 호출해서 결과 출력
P_eq, v_l, v_g, F_final = bisection_Peq(Tr, Ptest, P_right)
print("\n\nP_eq =", P_eq, "v_l =", v_l, "v_g =", v_g, "F_final =", F_final)

## maxwell 결과를 그래프에 표시
plt.figure(figsize=(7,5))
plt.plot(vgrid, Pgrid, label="VDW isotherm")
plt.axhline(P_eq, linestyle="--", color="black", label="Maxwell $P_{eq}$")
plt.scatter([v_l, v_g], [P_eq, P_eq], color="red", zorder=5)
plt.plot([], [], ' ', label=rf"$v_\ell = {v_l:.3f}$") #범례
plt.plot([], [], ' ', label=rf"$v_g = {v_g:.3f}$")
plt.plot([], [], ' ', label=rf"$P_{{eq}} = {P_eq:.3f}$")

plt.xlim(0.3, 10)
plt.ylim(-0.5, 2.0)
plt.xlabel(r"$v_r$")
plt.ylabel(r"$P_r$")
plt.title(rf"Maxwell construction ($T_r = {Tr}$)")
plt.grid(alpha=0.3)

plt.legend(loc="center right", frameon=True)

plt.show()
