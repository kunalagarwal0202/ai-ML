# Support Vector Regression (SVR)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)
y = y.reshape(10,1)
print(y)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()


X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)
print(X)
print(y)

# Training the SVR model on the whole dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

test_prediction=sc_y.inverse_transform((regressor.predict(sc_X.transform([[12]]))).reshape(1,1))
print(test_prediction)


# Predicting a new result
test_prediction2=sc_y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])).reshape(-1,1))
print(test_prediction2)
test_prediction2=np.round(test_prediction2,0)
print(test_prediction2)
y_test=np.array([175000])
print(y_test.dtype)
y_test.reshape(1,1)
print(y_test)
print()
from sklearn.metrics import accuracy_score
accuracy_svm=accuracy_score(test_prediction2,y_test)
print(f"accuracy for svm is {accuracy_svm}")

# Visualising the SVR results
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_y.inverse_transform(regressor.predict(X).reshape(-1,1)), color = 'blue')
plt.title('(Support vector)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()