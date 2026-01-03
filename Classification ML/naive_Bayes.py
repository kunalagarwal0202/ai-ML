import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('Social_network_Ads.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

x_train, x_test, y_train,y_test= train_test_split(x,y,test_size=0.25,random_state=42)

from sklearn.preprocessing import StandardScaler

sc= StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

from sklearn.naive_bayes import GaussianNB
reg= GaussianNB()
reg.fit(x_train, y_train)

y_pred= reg.predict(x_test)

from sklearn.metrics import accuracy_score , confusion_matrix
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))