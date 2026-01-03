import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset= pd.read_csv('Position_Salaries.csv')
x=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values


from sklearn.model_selection import train_test_split


#print(x)
#print(y)
from sklearn.linear_model import LinearRegression
len_reg= LinearRegression()
len_reg.fit(x,y)
y_pred=len_reg.predict(x)
from sklearn.preprocessing import PolynomialFeatures

poly_reg=PolynomialFeatures(degree=4)
x_poly=poly_reg.fit_transform(x)

line_reg2 =LinearRegression()
line_reg2.fit(x_poly,y)
y_pred1=line_reg2.predict(x_poly)

print(np.concatenate((y.reshape(len(y),1),y_pred.reshape(len(y_pred),1)),1))
print(np.concatenate((y.reshape(len(y),1),y_pred1.reshape(len(y_pred1),1)),1))


plt.scatter(x,y, color='red')
plt.plot (x, y_pred,color='black')
plt.plot(x, line_reg2.predict(x_poly), color='yellow' )
plt.plot (x, y_pred1,color='blue')
plt.plot(x)
plt.show()