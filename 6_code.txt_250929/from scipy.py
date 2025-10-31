from scipy.special import jv
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 500)
y = jv(0, x)  # 0차 베셀 함수

plt.plot(x, y)
plt.title('Bessel Function of the First Kind (Order 0)')
plt.grid(True)
plt.show()
