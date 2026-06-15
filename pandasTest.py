import numpy as np
import pandas as pd

sales_list=[10,20,50,30,50]
newSeries=pd.Series(sales_list, name="my first series")
print(newSeries)
print(newSeries.values)
floatSeries=newSeries.astype("float")
boolSeries=newSeries.astype("bool")
print(floatSeries)
print(boolSeries)

print(floatSeries[4])
print(floatSeries[0:4])
items=["apples","apples","cherry","milk","avacados"]
customeIndexedSeries=pd.Series(sales_list, index=items)
print(customeIndexedSeries)
print(customeIndexedSeries["apples":"milk"])
customeIndexedSeries.iloc[0:4]
testIndex=customeIndexedSeries.reset_index(drop=True)
print(testIndex.sort_values())
print(testIndex==10)
print(testIndex**5)
StringSeries=pd.Series(["test","test1","test2","testtest3"])
tested=StringSeries.astype("string")
print(tested.str.replace("test","find"))

print(testIndex.count())
print(testIndex.mean())
print(testIndex.unique())

test=None

newSereis=[1,2,3,4,5,pd.NA,6]
newSereis=pd.Series(newSereis)
print(newSereis)
print(newSereis.isna())
print(newSereis.fillna(newSereis.mean()))

