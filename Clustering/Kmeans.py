import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Mall_Customers.csv')
x=dataset.iloc[:,3:].values

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct= ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[0])],remainder='passthrough')
#x=ct.fit_transform(x)
#x=x[:,1:-1]


from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    clust= KMeans(n_clusters=i,init='k-means++',random_state=42)
    clust.fit(x)
    wcss.append(clust.inertia_)

#plt.plot(range(1,11), wcss)
#plt.show()

clust=KMeans(n_clusters=5,init='k-means++', random_state=42)
y_pred=clust.fit_predict(x)

xf=x
print(xf)
plt.scatter(xf[y_pred==0,0],xf[y_pred==0,1], s=100,c='red')

plt.scatter(xf[y_pred==1,0],xf[y_pred==1,1], s=100,c='blue')
plt.scatter(xf[y_pred==2,0],xf[y_pred==2,1], s=100,c='green')
plt.scatter(xf[y_pred==3,0],xf[y_pred==3,1], s=100,c='yellow')
plt.scatter(xf[y_pred==4,0],xf[y_pred==4,1], s=100,c='purple')

plt.show()

