import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 20, 500)
f=lambda x:np.sin(x) * np.exp(-0.1 * x)
plt.plot(x, f(x), color = 'r', linestyle = '--', linewidth = '2.5')
plt.ylim(-2, 2)

plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of sin(x)*exp(-0.1*x)')

x=[1,2,3]
y=[3,1,4]
plt.scatter(x,y, marker='s', c='b', edecolors='r')
plt.show()