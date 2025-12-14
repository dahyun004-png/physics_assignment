import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import pandas as pd
from sklearn.datasets import load_iris

iris_dataset = load_iris()


# 데이터 살펴보기
type(iris_dataset)
print("key value from iris_dataset:", iris_dataset.keys())

#print(iris_dataset['DESCR'])
print(iris_dataset['DESCR'][:500]+ "\n..")

print("feature_names value from iris_dataset:", iris_dataset['feature_names'])
print("target_names value from iris_dataset:", iris_dataset['target_names'])

iris=pd.read_csv("iris.csv")
iris.head()

X_iris = iris[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
y_iris = iris[["variety"]]

# 컬럼값 변경
X_iris_columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
X_iris.columns = X_iris_columns
X_iris.head(5)

y_iris
y_iris['variety'].unique()

# print("x_axis", X_iris_columns)
# print("y_axis", y_iris)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.3, random_state=0)
# 0의 의미: 처음에 정한 random 어쩌고
print("X_train 크기: {}".format(X_train.shape))
print("y_train 크기: {}".format(y_train.shape))

print("X_test 크기: {}".format(X_test.shape))
print("y_test 크기: {}".format(y_test.shape))

print(X_test)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)

X_train
y_train
print(y_train.shape)
print(y_train.values.ravel().shape)

## knn 알고리즘 training
knn.fit(X_train, y_train.values.ravel())

import numpy as np

Our_X = np.array([[5, 2.9, 1, 0.2]])
Our_X

prediction = knn.predict(Our_X)
print("예측: {}".format(prediction))

# y_test 를 1차원 matrix로 변경
y_test_flatten = np.array(y_test).flatten()

print("테스트 세트의 정확도: {:.2f}".format(np.mean(y_pred == y_test_flatten)))

print("테스트 세트의 정확도: {:.2f}".format(knn.score(X_test, y_test_flatten)))