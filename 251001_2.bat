import numpy as numpy
import matplotlib.pyplot as pyplot

x = np.linspace (0, np.pi, 100)
fun1 = lambda x: np.sin(x)
fun2 = lambda x: np.cos(x)

plt.figure()
plt.plot(x, fun1(x), c= 'k', label='sin(x)')
plt.plot(x, fun2(x), c='k', ls='--'. ; label='cos(x)')
plt.grid()
plt.xlabel('x')
plt.ylabel('sin(x) and cos(x)')
plt.title('trig functions')
plt.legend()

plt.figure()
plt.plot(fun1(),fun2(x), c='k')
plt.grid()
plt.xlabel('sin(x)')
plt.ylabel('cos(x)')
plt.title('cos(x) vs sin(x) for x=0 to pi')

plt.show()