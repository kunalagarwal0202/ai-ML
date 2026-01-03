import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Position_Salaries.csv')
x=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values

from sklearn.tree import DecisionTreeRegressor

tree= DecisionTreeRegressor(random_state=42)
tree.fit(x,y)
print(tree.predict([[6.5]]))

#random foresst regressor
from sklearn.ensemble import RandomForestRegressor

reg= RandomForestRegressor(random_state=0,n_estimators=100)
reg.fit(x,y)
print(reg.predict([[6.5]])) 

from sklearn.metrics import r2_score

print(r2_score(y,y))

print(y)


