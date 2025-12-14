import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

N = 100

X = np.linspace(0, 2*np.pi, N).reshape(N, 1)

y = np.sin(X)
y += 0.3*np.random.rand(N, 1)

polynomial = PolynomialFeatures(degree = 3, include_bias = False)
sin_new_feature = polynomial.fit_transform(X)

print("기존의 x[0]: ", X[1])
print("Feature가 추가된 x[0]: ", sin_new_feature[1])

print(sin_new_feature)