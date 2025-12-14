import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_openml
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge

boston = fetch_openml(name="boston", version=1, as_frame=True)
X_df = boston.data
y_data = boston.target.to_numpy(dtype=float)

print(X_df)
print("원 특성 수:", X_df.shape[1], "행:", X_df.shape(0))

poly = PolynomialFeatures(degree=2, include_bias=False)
X_data = poly.fit_transform(X_df.values)
feature_names = poly.get_feature_names_out(X_df.columns)

print("X data의 shape:", X_data.shape)
print("y data의 shape:", y_data.shape)
print(pd.DataFrame(X_data, columns=feature_names).head())

N = X_data.shape[0]
np.random.seed(3)
idx = np.random.permutation(N)
print(len(idx))

shuffle_X = X_data[idx]
shuffle_y = y_data[idx]

n = int(N*(3/4))
X_train = shuffle_X[:n]
y_train = shuffle_y[:n]
X_test = shuffle_X[n:]
y_test = shuffle_y[n:]

print(X_train.shape)
print(X_test.shape)
print(X_train.shape[0] + X_test.shape[0])