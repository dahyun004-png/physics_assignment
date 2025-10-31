# libraries
#1D로 그리면 아주 예쁜 가우시안 분포가 보일 것임!!
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#create data
size = 1000
df = pd.DataFrame({
    'x': np.random.normal(size=size),
    'y': np.random.normal(size=size)
})
df.head()

#df에서 x와 y를 가져옵니다.
x=df['x']
y=df['y']

#2D 히스토그램을 axs[0,0]에 그리기
plt.hist2d(x, y, bins=(1000,1000), cmap=plt.cm.jet)
plt.title('2D Histogram')

plt.show()