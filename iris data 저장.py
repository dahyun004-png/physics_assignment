import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
iris_df['target'] = iris['target']

iris_df.to_csv("iris_dataset.csv", index=False) #현재 작업 디렉토리에 저장

from sklearn import datasets

iris = datasets.load_iris()

import matplotlib.pyplot as plt

_, ax = plt.subplots()
scatter = ax.scatter(iris.data[:,0], iris.data[:,3], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[3])
_=ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)

plt.show()