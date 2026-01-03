import numpy as np
import matplotlib.pyplot  as plt
import pandas as pd

dataset= pd.read_csv('Wine.csv')

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train= sc.fit_transform(x_train)
x_test=sc.transform(x_test)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda=LinearDiscriminantAnalysis(n_components=1)
x_train=lda.fit_transform(x_train, y_train)
x_test=lda.transform(x_test)


from sklearn.linear_model import LogisticRegression
reg=LogisticRegression(random_state=42)
reg.fit(x_train,y_train)
y_pred= reg.predict(x_test)

from sklearn.metrics import accuracy_score, confusion_matrix
print(accuracy_score(y_test, y_pred))