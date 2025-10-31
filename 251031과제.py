# 2330002 고다현
import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import trapezoid

# 1. 데이터 읽어들이기
bins, count = [], []
with open("hist2.csv", "r") as f:
    for line in f.readlines():
        _b, _c = [float(i) for i in line.split(",")]
        bins.append(_b)
        count.append(_c)

# 2. 데이터를 NumPy 배열로 변환
x_data = np.array(bins)
y_data = np.array(count)

# 3. 모델 함수 (Gaussian function 정의)
def particle(x, a, b, c):
    return a * np.exp(-((x - b)**2) / (2 * c**2))

# 이중 가우시안 함수 정의 (두 입자 A, B의 합)
# 측정값은 입자 A의 실제 분포와 입자 B의 실제 분포가 합쳐진 결과
# (a1, b1, c1) for Particle A, (a2, b2, c2) for Particle B
def double_gaussian(x, a1, b1, c1, a2, b2, c2):
    return particle(x, a1, b1, c1) + particle(x, a2, b2, c2)


# 4. 초기 매개변수 추정
# 피크 A (왼쪽, 빨간색): 
#   - 높이(a1): 약 950 (y축)
#   - 중심(b1): 약 1.0 (x축)
#   - 폭(c1): 좁음, 약 0.2
# 피크 B (오른쪽, 파란색): 
#   - 높이(a2): 약 550 (y축)
#   - 중심(b2): 약 2.0 (x축)
#   - 폭(c2): 넓음, 약 0.5
initial_guesses = [950, 1.0, 0.2, 550, 2.0, 0.5]


# 5. 피팅 수행 (Curve Fitting)
# curve_fit을 사용하여 이중 가우시안 함수를 데이터에 맞추기
popt, pcov = curve_fit(double_gaussian, x_data, y_data, p0=initial_guesses)
    

# 최적화 파라미터 분리
params_A = popt[:3]  # a1, b1, c1
params_B = popt[3:]  # a2, b2, c2

# 6. 적분 및 생성비 계산
x_fit = np.linspace(x_data.min(), x_data.max(), 500) #x_data의 최솟값부터 최댓값까지를 500개의 균일한 간격으로 나누어 부드러운 곡선을 그릴 새로운 x축 배열 생성

y_fit_A = particle(x_fit, *params_A) # 입자 A의 가우시안 곡선
y_fit_B = particle(x_fit, *params_B) # 입자 B의 가우시안 곡선

# 적분값 = 총 빈도수 (사다리꼴 공식을 이용한 수치 적분)
integral_A = trapezoid(y_fit_A, x_fit) 
integral_B = trapezoid(y_fit_B, x_fit)

# 생성비 계산
production_ratio_A_to_B = integral_A / integral_B


# 7. 그래프 출력
y_fit_total = double_gaussian(x_fit, *popt) #이중 가우시안 함수 전체의 y값 계산(검정색 선)

plt.figure(figsize=(10, 6))

 # 원본 데이터 출력 (막대 그래프)
plt.bar(x_data, y_data, width=x_data[1]-x_data[0], color='gray', alpha=0.7, label='Measured Spectrum')

# 입자 A (빨강 곡선) 출력
plt.plot(x_fit, y_fit_A, color='red', linewidth=2, label=f'Particle A Fit (N={integral_A:.0f})')

# 입자 B (파랑 곡선) 출력
plt.plot(x_fit, y_fit_B, color='blue', linewidth=2, label=f'Particle B Fit (N={integral_B:.0f})')

# 총 피팅 모델 (검은색 곡선) 출력
plt.plot(x_fit, y_fit_total, color='black', linewidth=2, linestyle='-', label='Total Fit')

plt.title('Energy Spectrum Double Gaussian Fitting of particle A & B')
plt.xlabel('Energy (x-axis)')
plt.ylabel('Count (y-axis)')
plt.grid(True, linestyle='--')
plt.legend()
plt.show()

# 생성비 출력
print(f" * 두 입자의 생성비 (A : B) = {production_ratio_A_to_B:.2f} : 1")