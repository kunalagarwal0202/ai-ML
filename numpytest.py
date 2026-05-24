import numpy as np

salesList=[1,5,6,7,44,66,34,6666,789]
sales=np.array((1,2,4,5,6,7,89,9))
sales=np.array([1,2,5,6,7,8])
salesArray=np.array(salesList)

print(salesArray)
print(sales)
print(sales.__class__)
print(f"dimenstion of our numpy array sales {sales.ndim}")
print(f"shape of our numpy array sales {sales.shape}")
print(f"size of our numpy array sales {sales.size}")
print(f"data type of our numpy array sales {sales.dtype}")

testOnes=np.ones((6,6),dtype=int)
print(testOnes)

testZeroes=np.zeros((6,6))
print(testZeroes)

testArray=np.arange(0,10)
testArray2=np.arange(50,500,5)
print(testArray)
print(testArray2)

testArrayLin=np.linspace(1,100,20)
print(testArrayLin)

print(np.arange(1,11).reshape(2,5))


product_array=np.array([["fruits","vegetables","oranges","apples","mangoes"],
                       ["milk1","cereal","cookies1","food","biscuits1"],
                       ["milk2","cereal","cookies2","food","biscuits2"],
                       ["milk3","cereal","cookies3","food","biscuits3"],
                       ["milk4","cereal","cookies4","food","biscuits4"],
                       ["milk5","cereal","cookies5","food","biscuits5"]])
print(product_array)
print(product_array[0,1])
print(product_array[1,1])

print(product_array[:1,:2])

print(product_array[2:5,1:4])


print(testArrayLin+2)
print(testArrayLin*2)

print(testArrayLin)
print(product_array)

print(testArrayLin ==0)

print(testArrayLin[(testArrayLin <50 )|( testArrayLin >70)])
print(testArrayLin)

product_array[0,1]="chillies"
print(product_array[0,1])

product_array_stock=np.array([1,0,8,5,6,0,4])
stock_array=np.where(product_array_stock>0,"IN-stock","out of stock")
print(stock_array)

print(product_array_stock.sum())
print(product_array_stock.mean())
print(product_array_stock.min())
print(product_array_stock.max())

print(np.median(product_array_stock))
print(np.percentile(product_array_stock,90))
print(np.unique(product_array_stock))
print(np.sqrt(product_array_stock))
product_array_stock.sort()
print(product_array_stock)

testArray=np.array([[1,56,78,90,5,23,89],[91,560,4,8,5,0,2]])
print(testArray)
testArray.sort(axis=0)
print(testArray)


[1,1,1]
[1,1,1]
[1,1,1]

