import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)

y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

logreg = LogisticRegression(solver='lbfgs', max_iter=1000, C=1000)
logreg.fit(X_scaled, y)

X_range = np.linspace(X_scaled.min(), X_scaled.max(), 100).reshape(-1, 1)
y_prob = logreg.predict_proba(X_range)[:, 1]

plt.scatter(X_scaled, y, label = 'Data points', alpha = 0.7)
plt.plot(X_range, y_prob, color='red', label='Logistic Regression', linewidth = 2)
plt.ylabel('Cancer (1) or Not (0)', fontsize = 12)
plt.xlabel('Tumor Size (scaled)',fontsize = 12)
plt.title('Logistic Regression Predictions', fontsize = 14)
plt.legend()
plt.show()

size_to_predict = np.array([3.46]).reshape(-1, 1)
size_to_predict_scaled = scaler.transform(size_to_predict)
predicted = logreg.predict(size_to_predict_scaled)
print(f"Prediction for tumor size 3.46cm: {predicted[0]} (0=Not Cancerous, 1=Cancerous)")