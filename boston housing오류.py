import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge

# 1. 데이터 불러오기
california = fetch_california_housing(as_frame=True)
X_df = california.data
y_data = california.target.to_numpy(dtype=float)

print(X_df.head())
print("원 특성 수:", X_df.shape[1], "행:", X_df.shape[0])

# 2. 다항 특성 생성 (degree=2)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_data = poly.fit_transform(X_df.values)
feature_names = poly.get_feature_names_out(X_df.columns)

print("X data의 shape:", X_data.shape)
print("y data의 shape:", y_data.shape)
print(pd.DataFrame(X_data, columns=feature_names).head())

# 3. 데이터 섞기
N = X_data.shape[0]
np.random.seed(3)
idx = np.random.permutation(N)
print(len(idx))

shuffle_X = X_data[idx]
shuffle_y = y_data[idx]

# 4. Train/Test 분할 (3/4 : 1/4)
n = int(N * (3/4))
X_train = shuffle_X[:n]
y_train = shuffle_y[:n]
X_test  = shuffle_X[n:]
y_test  = shuffle_y[n:]

print(X_train.shape)
print(X_test.shape)
print(X_train.shape[0] + X_test.shape[0])

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

X_mean = X_train.mean(axis = 0)
X_std = X_train.std(axis = 0)
X_std[X_std == 0] = 1.0

X_train_s = (X_train - X_mean) / X_std
X_test_s = (X_test - X_mean) / X_std

reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

def MSE(real, predict):
    return ((real - predict) ** 2).mean()

def get_top_botton(data, count):
    idx_sorted = np.argsort(data)
    top_idx = idx_sorted[-count:]
    bottom_idx = idx_sorted[:count]
    top_vals = [data[i] for i in top_idx]
    bottom_vals = [data[i] for i in bottom_idx]
    return top_vals, bottom_vals

print("\n=== OLS (LinearRegression) ===")
print("Training R^2 score:{:0.2f}".format(reg.score(X_train, y_train)))
print("Test R^2 score: {:0.2f}".format(reg.score(X_test, y_test)))
print('Mean squared error:{:0.2f}'.format(MSE(y_test, y_pred)))

W = reg.coef_
top_3_idx = np.argsort(W)[-3:]
bottom_3_idx = np.argsort(W)[:3]
print("OLS 가장 높은 W 3개 =>", ["{:0.2f}".format(W[i]) for i in top_3_idx])
print("OLS 가장 낮은 W 3개 =>", ["{:0.2f}".format(W[i]) for i in bottom_3_idx])

ridge01 = Ridge(alpha=0.1).fit(X_train_s, y_train)
ridge05 = Ridge(alpha=0.5).fit(X_train_s, y_train)
ridge1 = Ridge(alpha=1.0).fit(X_train_s, y_train)
ridge10 = Ridge(alpha=10.0).fit(X_train_s, y_train)

def report_ridge(name, model):
    pred = model.predict(X_test_s)
    print(f"[alpha={name}] Training R^2: {model.score(X_train_s, y_train):0.2f}) |"
          f"Test R^2: {model.score(X_test_s, y_test):0.2f} |"
          f"MSE: {MSE(y_test, pred):0.2f}")
    
print("\n lambda 값에 대한 train-test R^2, MSE값")
report_ridge("0.1", ridge01)
report_ridge("0.5", ridge05)
report_ridge("1.0", ridge1)
report_ridge("10.0", ridge10)

alpha = [i / 10 for i in range(1, 101)]
train_score, test_score = [], []

for a in alpha:
    m = Ridge(alpha=a)
    m.fit(X_train_s, y_train)
    train_score.append(m.score(X_train_s, y_train))
    test_score.append(m.score(X_test_s, y_test))

plt.figure()
plt.grid(linestyle='--')
plt.plot(alpha, train_score, label="Train Score")
plt.plot(alpha, test_score, label="Test Score")
plt.title("Ridge Score (Boston, degree=2, manual standardization)")
plt.legend(loc='best')
plt.xlabel("Alpha")
plt.ylabel("R^2 Score")
plt.ylim(0, 1)
plt.show()

coef_ridge01 = ridge01.coef_
coef_ridge05 = ridge05.coef_
coef_ridge1 = ridge1.coef_
coef_ridge10 = ridge10.coef_

reg_std = LinearRegression().fit(X_train_s, y_train)
W_std = reg_std.coef_

plt.figure(figsize=(13, 7))
plt.plot(W,                 'p', label="OLS (no scaling)")
plt.plot(W_std,             'x', label="OLS (std space)")
plt.plot(coef_ridge01,      '.', label="Ridge alpha=0.1 (std)")
plt.plot(coef_ridge05,      'v', label="Ridge alpha=0.5 (std)")
plt.plot(coef_ridge1,        'o', label="Ridge alpha=1 (std)")
plt.plot(coef_ridge10,      'p', label="Ridge alpha=10 (std)")

stacked = np.concatenate([W_std, coef_ridge01, coef_ridge05, coef_ridge1, coef_ridge10])
max_abs = np.max(np.abs(stacked))
plt.ylim(-1.1*max_abs,1.1*max_abs)

plt.legend(loc='center', bbox_to_anchor=(1.2, 0.5))
plt.ylabel("W values")
plt.title("Coefficient Comparison (Boston degree=2, std space)")
plt.tight_layout()
plt.show()