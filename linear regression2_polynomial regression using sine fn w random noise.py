import numpy as np
from matplotlib import pyplot as plt

print(np.pi)

N = 100

X = np.linspace(0, 2*np.pi, N).reshape(N,1)
print(X[:5])

y = np.sin(X)
##plt.plot(X, y)
##plt.scatter(X, y)
##plt.show()

np.random.seed(1)
y += 0.3*np.random.rand(N,1)

##plt.scatter(X, y)
##plt.title('sine wave noise data')
##plt.show()

y = np.sin(X)
plt.plot(X,y)

np.random.seed(1)
y += 0.3*np.random.rand(N,1)

##plt.scatter(X,y)
##plt.title('sine wave data')
##plt.show()

# shuffle data
np.random.seed(10)

# N은 100이므로 0~99까지의 수를 섞어준다
idx = np.random.permutation(N)
print(idx)

shuffle_X = X[idx]
shuffle_y = y[idx]

print(shuffle_X[:3])
print(shuffle_y[:3])

#3:1의 비율로 train test를 나눔
n = int(N*(3/4))  #75% train시킴!!

# train data
X_train = shuffle_X[:n]
y_train = shuffle_y[:n]

#test data
X_test = shuffle_X[n:]
y_test = shuffle_y[n:]

#plot
plt.scatter(X_train, y_train, label='train')
plt.legend()
plt.title('sine wavae train data')
plt.show()

plt.scatter(X_test, y_test, label='test')
plt.legend()
plt.title('sine wave test data')
plt.show()