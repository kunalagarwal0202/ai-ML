import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Mall_Customers.csv')
x=dataset.iloc[:,3:].values
from sklearn.cluster import DBSCAN
db=DBSCAN(eps=10,min_samples=5)
y_pred=db.fit_predict(x) 
xf=x
print(y_pred)
plt.scatter(xf[y_pred==-1,0],xf[y_pred==-1,1], s=100,c='purple')
plt.scatter(xf[y_pred==0,0],xf[y_pred==0,1], s=100,c='red')

plt.scatter(xf[y_pred==1,0],xf[y_pred==1,1], s=100,c='blue')
plt.scatter(xf[y_pred==2,0],xf[y_pred==2,1], s=100,c='green')
plt.scatter(xf[y_pred==3,0],xf[y_pred==3,1], s=100,c='yellow')

plt.show()