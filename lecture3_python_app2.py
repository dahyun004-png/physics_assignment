import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import numpy as np
import matplotlib.pyplot as plt
x = []
y = []

with open("input.csv", "r") as f:
    for line in f.readlines():
        _x, _y = [float(i) for i in line.split(" ")]
        x.append(_x)
        y.append(_y)

degs = [1,2,3,4,5,8,14,18]
new_x = np.linspace(0,1)
plt.figure(figsize=(8, 10))
for idx, deg in enumerate(degs):
    #계수 연산
    coef = np.polyfit(x,y,deg)
    #연산한 계수를 함수로 만듦
    fit = np.poly1d(coef)
    #R^2값 계산
    sst = np.sum(np.power(y - np.average(y), 2))
    ssr = np.sum(np.power(y - fit(x), 2))
    sqr = 1 - (ssr / sst)
    print(f"======= DEG: {deg}, R^2:{sqr:.3f} =======")
    print(coef)

    #서브플롯 명령
    ax = plt.subplot(4, 2, idx + 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(-1, 1)
    ax.text(0.05, -0.9, f"DEG: {deg}, $R^2$: {sqr:.3f}", fontsize=10)
    ax.plot(x, y, ".k")
    ax.plot(new_x, fit(new_x), "--r", label="DEG: {}".format(deg))
plt.savefig("01_data_fitting.png", bbox_inches="tight")
plt.show()