import pandas as pd

sales=[0,1,4,5,67,89,00,45,12,1223,455]
sales_series=pd.Series(sales,name="sales seires")
print(sales_series)
print(sales_series.dtype)
print(sales_series.name)
print(sales_series.values)
test_Sereis=sales_series.astype("float32")
print(test_Sereis)
bool_series=sales_series.astype("bool")
print(bool_series)

print(test_Sereis[9])
print(test_Sereis[5:9])
print(sales_series)
new_custom_series=pd.Series(sales,name="custome_indexed_series")
print(new_custom_series)
new_custom_series.index=["a","b","c","d","e","f","g","h","i","j","k"]
print(new_custom_series["b":"j"])
print(new_custom_series.iloc[10])
print(new_custom_series.loc["b"])

print(new_custom_series.reset_index(drop=True))

sorted_sries=new_custom_series.sort_index()
print(sorted_sries)

sorted_values_serire=new_custom_series.sort_values(ascending=False)
print(sorted_values_serire)
print(sorted_values_serire+2)
print(sorted_values_serire.add(2))
string_series=pd.Series(["apples","bananas","chocolates","milk","lemons"])

print(string_series.str.contains("a"))
print(string_series.str.upper())
print(string_series.str.lower())
print(string_series.str.strip("a"))
print(string_series.str.replace("a","t"))

print(new_custom_series.count())

print(new_custom_series.first)
print(new_custom_series.mean())
print(new_custom_series.median())
print(new_custom_series.min())

print(new_custom_series.std())
print(new_custom_series.var())
print(new_custom_series.prod())

print(new_custom_series.nunique())

nan_series=[0,2,3,5,pd.NA,9]
nan_series_1=pd.Series(nan_series)
print(nan_series_1.isna())
print(nan_series_1.dropna())
print(nan_series_1.fillna(0))
print(nan_series_1.fillna(nan_series_1.mean()))

def discount(price):
    return price*0.9

print(nan_series_1.apply(discount))




# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


#visualizing the data
plt.scatter(X_train, y_train, color = 'red')
plt.scatter(X_test, y_test, color = 'yellow')
plt.plot(X_train, y_train, color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test, y_test, color = 'red')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


plt.scatter(X_test, y_test, color = 'red')
plt.scatter(X_train, y_train, color = 'blue')
plt.show()