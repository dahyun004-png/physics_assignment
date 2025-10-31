import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import matplotlib.pyplot as plt

x=[]
y=[]

with open ("input.csv", "r") as f:
    for line in f.readlines():
        items = line.split(" ")
        x.append(float(items[0]))
        y.append(float(items[1]))

if __name__=="__main__":
    plt.scatter(x,y)
    plt.xlim(0,1)
    plt.ylim(-1.5, 1.5)
    plt.grid(True)

    plt.show()

    ####################
    x=[]
    y=[]

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 20, 500)
f=lambda x:np.sin(x) * np.exp(-0.1 * x)
plt.plot(x, f(x))
plt.ylim(-2, 2)
plt.show()