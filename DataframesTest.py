import pandas as pd
print(pd.DataFrame(
   {  "id":[1,2,3,4,5,6,7,8],
    "Family":["apples","bananas","chillies","oranges","guava","mangoes","milk","grapes"]
   }
))
dataframe=    pd.read_csv("Social_Network_Ads.csv")
#print(dataframe)

print(dataframe.head(10))
print(dataframe.tail())
print(dataframe.sample())


print(dataframe.Age)
print(dataframe.EstimatedSalary)

x=dataframe.iloc[:,0:2]
print(x)

y=dataframe.iloc[:,-1]
print(y)

print(dataframe.info())
print(dataframe.describe())



#LinearSearch
list=[1,2,3,45,6,7,8,9,10,23,56,89,45]
i=0

print(list.__sizeof__)
def linearSearch(input,list):



    for i in range(0,len(list)):
        if list[i]==input:
            print(f"element found at index{i+1}")
            break
        else:
            print("not found")

#space complexity

#time complexity




linearSearch(10,list)
