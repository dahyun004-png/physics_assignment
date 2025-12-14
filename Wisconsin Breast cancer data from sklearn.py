import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the breast cancer dataset
br_cancer = load_breast_cancer()

print(br_cancer)
print(br_cancer['DESCR'])
print(br_cancer.feature_names)
print(br_cancer.data)

# convert data to pandas DataFrame
x = pd.DataFrame(br_cancer.data, columns=br_cancer.feature_names)
y = pd.Series(br_cancer.target)

# Display the first few rows of the DataFrame
print(x.head())

#Split data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1234)

# Scale the data
scaler = StandardScaler()
x_train_sclaed = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

#Plot one feature against the target
plt.scatter(x['worst concave points'], y, alpha = 0.5, label = 'Data points')
plt.ylabel('malignant (1) or benign (0)', fontsize = 12)
plt.xlabel('worst concave points', fontsize = 12)
plt.title('Breast Cancer Diagnosis vs. Worst Concave Points', fontsize = 14)
plt.legend()
plt.show()

# Sigmoid fn
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x_sigmoid = np.arange(-10., 10., 0.2)
sig = sigmoid(x_sigmoid)

plt.plot(x_sigmoid, sig)
plt.title('Sigmoid Function')
plt.show()

#Logistic regression model
model = LogisticRegression(solver = 'lbfgs', max_iter = 1000).fit(x_train_scaled, y_train)

X = x[['worst concave poitns']].values
y = y.values

X_scaled = scaler.fit_transform(X)

logreg = LogisticRegression(C = 1000, max_iter = 1000)
logreg.fit(X_scaled, y)

example_df = pd.DataFrame({
    'worst_concave_points': X.flatten(),
    'diagnosis': y
})

example_df['logistic_preds'] = logreg.predict_proba(X_scaled)[:, 1]
example_df = example_df.sort_values(by='worst_concave_points')

#Plot logistic regression predictions
plt.scatter(example_df['worst_concave_points'], example_df['diagnosis'], label='Data points')
plt.plot(example_df['worst_concave_points'], example_df['logistic_preds'], color='red', label='Logistic Reression')
plt.ylabel('malignant (1) or benign (0)', fontsize = 12)
plt.title('Logistic Regression Predictions')
plt.legend()
plt.show()

y_pred = model.predict(x_test_scaled)

accuracy = model.score(x_test_scaled, y_test)
print(f"Model accuracy: {accuracy:.2f}")