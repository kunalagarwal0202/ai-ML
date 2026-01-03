import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split



dataset = pd.read_csv('Data.csv')
x=dataset.iloc[:, :-1].values
y=dataset.iloc[:,-1].values


print(x)
imputer=SimpleImputer(missing_values=np.nan, strategy='median')
imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

print(x)

ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])], remainder='passthrough')
x=(ct.fit_transform(x))

le =LabelEncoder()
y=le.fit_transform(y)

x_train, x_test, y_train, y_test=split =train_test_split(x,y,test_size=0.2, random_state=16)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_test[:,3:] =sc.fit_transform(x_test[:,3:])   
x_train[:,3:] =sc.fit_transform(x_train[:,3:])  

print(x_train)