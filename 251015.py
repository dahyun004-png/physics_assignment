import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)

def g(func, x):
    y = []
    h = 0.01
    for _x in x:
        y.append((func(_x + h) - func(_x)) / h) #도함수의 정의
    return np.array(y)

if __name__ == "__main__":
    x = np.linspace(0,10*np.pi, 2000)

    plt.figure(figsize=(10, 5))
    plt.title("sin(x) and its derivative (cos(x))")
    plt.xlim(0, 10*np.pi)
    plt.ylim(-1.2, 1.2)

    # 원래 함수 sin(x)
    plt.plot(x, f(x), label="sin(x)", linewidth=2)

    # 수치미분 (≈ cos(x))
    plt.plot(x, g(f, x), label="Derivative of sin(x)", linestyle='--', linewidth=2)


    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend(loc="center right")
    plt.tight_layout()
    plt.show()
