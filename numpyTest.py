import numpy as np

sales=[1.7,2.9,3,4.08,5.7,6.5]
new_array=np.array(sales)
print(new_array.__class__)
print(sales.__class__)
print(new_array.shape)
print(new_array.dtype)
print(new_array.size)
print(new_array.ndim)

ones_array=np.ones(4,)
zeros_array=np.zeros(5,)
print(ones_array)
print(zeros_array)

arramge_array=np.arange(0,11,2)
print(arramge_array)

linspace_array=np.linspace(0,50,5)
print(linspace_array)

print(arramge_array[3])

dim_array=np.ones((4,2,3,3))
print(dim_array.shape)
print(dim_array.size)

test_dim=dim_array.reshape(2,18,2)
print(test_dim)

test_array=np.array([[1,2,3,4,5,6,7,8,9,10],
                    [11,12,13,14,15,16,17,18,19,20],
                    [21,22,23,24,25,26,27,28,29,30]])
test_element=test_array[1,2]
print(test_element)
new_array=test_array[0:2,2:6]
print(new_array**3)
boolean_array=test_array==20
bool_array=test_array>=10
print(bool_array)
print(boolean_array)
print(test_array)
print("------------------------")
test=test_array[(test_array>=5) & (test_array<=11)& (test_array<=8)]
print(test)
test[0]=1
print(test)
test[test>5]=8
print(test)

stock=np.array([1,2,3,4,0,10,0,1])
stock_details=np.where(stock>0,"Stock  available","stock not available")
print(stock_details)
total=stock.sum()
print(total)
print(stock.mean())
print(stock.max())
print(stock.min())
print(np.median(stock))
print(np.percentile(stock,100))
print(np.unique(stock))
print(np.sqrt(stock))
print(stock.sort())
print(stock)

import pandas as pd
test_series=pd.Series([1,2,3,4,56,7],name="new series")
print(test_series)