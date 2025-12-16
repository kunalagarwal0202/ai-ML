import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Mall_Customers.csv')
x=dataset.iloc[:,3:].values

import scipy.cluster.hierarchy as sch
#dendrogram =sch.dendrogram(sch.linkage(x,method='ward'))


from sklearn.cluster import AgglomerativeClustering

hc =AgglomerativeClustering(n_clusters=5, linkage='ward')
y_pred=hc.fit_predict(x)

xf=x
print(xf)
plt.scatter(xf[y_pred==0,0],xf[y_pred==0,1], s=100,c='red')

plt.scatter(xf[y_pred==1,0],xf[y_pred==1,1], s=100,c='blue')
plt.scatter(xf[y_pred==2,0],xf[y_pred==2,1], s=100,c='green')
plt.scatter(xf[y_pred==3,0],xf[y_pred==3,1], s=100,c='yellow')
plt.scatter(xf[y_pred==4,0],xf[y_pred==4,1], s=100,c='purple')
plt.show()