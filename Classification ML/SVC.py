import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('Social_network_Ads.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)


from sklearn.svm import SVC
reg= SVC(kernel='rbf', random_state=42)

reg.fit(x_train, y_train)

y_pred=reg.predict(x_test)

from sklearn.metrics import confusion_matrix, accuracy_score

print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))

from matplotlib.colors import ListedColormap
x_set,y_set=sc.inverse_transform(x_train), y_train
X1, X2=np.meshgrid(np.arange(start=x_set[:,0].min()-10, stop=x_set[:,0].max()+10, step=0.25),
                   np.arange(start=x_set[:,1].min()-1000, stop=x_set[:,1].max()+1000,step=0.25))

plt.contourf(X1,X2, reg.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),alpha=0.75, cmap=ListedColormap(('red','green')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0], x_set[y_set==j,1],c=ListedColormap(('red','green'))(i),label=j)
plt.show()