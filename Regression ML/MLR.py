import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

dataset =pd.read_csv('50_Startups.csv')
x= dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


ct =ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[3])],remainder='passthrough')
x=(ct.fit_transform(x))
x=x[:,1:]
#print(x)
#print(y)
#print(ct.get_feature_names_out())



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=16)
#x_train = scaler.fit_transform(x_train)
#x_test = scaler.fit_transform(x_test)
regressor= LinearRegression()
regressor.fit(x_train,y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None)
y_pred=regressor.predict(x_test)
np.set_printoptions(precision=2)
print(np.concatenate    (   (y_pred.reshape(len(y_pred),1),  y_test.reshape(len(y_test),1))  ,1)  )

from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("MAE:", mae)
print("RMSE:", rmse)