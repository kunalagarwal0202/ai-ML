import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Wine.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
#x_train=pca.fit_transform(x_train)
#x_test=pca.transform(x_test)

from sklearn.manifold import TSNE
classification= TSNE(n_components=3, perplexity=10, early_exaggeration=12, learning_rate='auto')
x_train=classification.fit_transform(x_train)
x_test=classification.fit_transform(x_test)

from sklearn.linear_model import LogisticRegression
reg= LogisticRegression(random_state=0)
reg.fit(x_train, y_train)
y_pred=reg.predict(x_test)


from sklearn.metrics import accuracy_score, confusion_matrix
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


from matplotlib.colors import ListedColormap
#x_set,y_set= x_train,y_train
#1, X2= np.meshgrid(np.arange(start=x_set[:,0].min( )-1, stop=x_set[:,0].max()+1, step=0.1),
                    #np.arange(start=x_set[:,1].min()-1, stop=x_set[:,1].max()+1, step=0.1))

#plt.contourf(X1,X2, reg.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             #alpha=0.75, cmap=ListedColormap(('red','blue','green')))
#plt.xlim(X1.min(), X1.max())
#plt.ylim(X2.min(),X2.max())
#plt.show()