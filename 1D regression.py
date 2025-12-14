# Graph 상에 임의로 Dot을 찍어서 차수에 따른 그래프의 변화를 확인한다
# 데이터와 1차(선형) 회귀

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(1, 11).reshape(10, 1)
y = np.array([7, 8, 7, 13, 16, 15, 19, 23, 8, 21]).reshape(10, 1)

plt.plot(X, y, 'ro') # bo = blue + circle / use go (green circle)

axes = plt.gca() #현재 figure의 축을 가져옴
axes.set_ylim([0, 30])

plt.show()

reg = LinearRegression()
reg.fit(X,y)

w0 = reg.intercept_
w1 = reg.coef_

print('w0: ', w0)
print('w1: ', w1)

y_pred = reg.predict(X)

plt.plot(X, y, 'ro')
plt.plot(X, y_pred)

# gca = 그래프의 '축'을 설정
axes = plt.gca()
axes.set_xlim([0, 11])
axes.set_ylim([0, 30]) #gca
plt.show()

#2차원 그래프, 2차(Quadratic) 다항 회귀
# np_c => 1차원 배열 두개를 col 방향으로 나열해서 concatentation
X_2 = np.c_[X, X**2] #다항 회귀에서 기존 입력값 X에 "제곱항" 추가
print(X_2)

reg = LinearRegression()
reg.fit(X_2, y)

w0 = reg.intercept_
w = reg.coef_

print('w0: ', w0)
print('w1: ', w[0][0])
print('w2: ', w[0][1])

print(reg.coef_)

y_pred_2 = reg.predict(X_2)

plt.plot(X, y, 'ro')
plt.plot(X_2[:,0], y_pred_2)

# gca = 그래프의 '축'을 설정
axes = plt.gca()
axes.set_xlim([0, 11])
axes.set_ylim([0, 30]) # gca를 이용해 y의 범위를 0~30으로 늘려준다
plt.show()

#3차원 그래프, 3차(Cubic) 다항 회귀 - PolynomialFeatures 사용
# np_c => 1차원 배열 두개를 col 방향을 나열해서 concatentation
X_3 = np.c_[X, X**2, X**3]
print(X_3)

from sklearn.preprocessing import PolynomialFeatures
polynomial = PolynomialFeatures(degree = 3, include_bias = False)
X_3_poly = polynomial.fit_transform(X)

reg = LinearRegression()
reg.fit(X_3_poly, y)

w0 = reg.intercept_w = reg.coef_

print(w)

print('w0: ', w0)
print('w1: ', w[0][0])
print('w2: ', w[0][1])
print('w3: ', w[0][2])

x_2 = np.array([2,4,8])
x_2

y_2 = (np.array([2,4,8]) @ w.reshape(-1,1)) + w0
y_2

print(w[0][2]*8 + w[0][1]*4 + w[0][0]*2 + 7.2)

y_pred_3 = reg.predict(X_3_poly) 

plt.plot(X, y, 'ro')
plt.plot(X, y_pred_3)

axes = plt.gca()
axes.set_xlim([0,11])
axes.set_ylim([0,30])
plt.show()

X_new = np.arange(-5,15,0.01).reshape(-1,1)

from sklearn.preprocessing import PolynomialFeatures

polynomaia = PolynomialFeatures(degree = 3, include_bias = False)
X_new_3 = polynomial.fit_tranform(X_new)

y_pred_3 = (X_new_3 @ w.reshape(-1,1)) + w0

plt.plot(X_new, y_pred_3)

plt.plot(X, y, 'ro')
plt.plot(X_new, y_pred_3)

axes = plt.gca()
axes.set_xlim([0, 11])
axes.set_ylim([0, 30])
plt.show()