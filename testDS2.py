myList=["apples","oranges","banana","milk","chillies",1,2,3,5,6]

myList.append("potato")
myList.append("tomato")
myList.append("potato")
myList.insert(4,"chocolate")
myList.remove("chocolate")
myList.remove(1)
print(myList)
test=1
print(test.__class__)

numList=[1,2,3,4,5,7,6,0]

print(sum(numList))
print(len(numList))
print(min(numList))
print(max(numList))


print(numList[3])
newList=numList.sort(reverse=True)
print(numList)
numList.reverse()
print(numList)

myset={1,2,3,5,7,7,8,8}


myset.add(10)
myset.remove(1)
print(myset)
print(2 in myset)
print(20 in myset)

myDict={"key":"value","age":20, "name":"python","good":True}
myDict2={"key2":"value2","age2":45}
forDict={1:2,3:45,5:6}
print("---------------------------")

print(forDict.items())

for x, y in forDict.items():
    print(x+y)

def add(value):
    return value+2

mydict3={x:add(x) for x in {1:2,3:4,5:6}}
print(mydict3)


print(myDict)
print(myDict["key"])
print(myDict.keys())
print(myDict.values())


myDict["age"]=35
print(myDict)

test=12 
test="mytest"
test2="mytest"



print(test)
x=[1,2,3,4,5,6,7]
myMap=list(map(add,x))
print(myMap)