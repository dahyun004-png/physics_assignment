from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

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