import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset =pd.read_csv('Position_Salaries.csv')
x=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values
y= y.reshape(len(y),1)


#feature scaling
from sklearn.preprocessing import StandardScaler
scy= StandardScaler()
y= scy.fit_transform(y)

scx= StandardScaler()
x=scx.fit_transform(x)
print(x)
print(y)

from sklearn.svm import SVR

regressor = SVR(kernel='rbf')
regressor.fit(x,y)

y_pred=scy.inverse_transform(regressor.predict(scx.transform([[6.5]])).reshape(-1,1))

print(y_pred)

plt.scatter(scx.inverse_transform(x),scy.inverse_transform(y),color='red')

plt.plot(scx.inverse_transform(x), scy.inverse_transform((regressor.predict(x)).reshape(-1,1)), color='blue')
plt.show()




