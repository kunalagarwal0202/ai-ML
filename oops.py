import abc


class planet():
    def __init__(self,name="earth",distance=1000,radius=6500):
        self.name = name
        self.distance =distance
        self.radius=radius

#__keyword__--->belongs to python         
    
    def revolve(self):
        print(f" my planet  {self.name} is revolving")
        print(f" my planet  {self.radius} is revolving")
        print(f" my planet  {self.distance} is revolving")
    


    def rotate(self, rotationspeed):
        print(f"myplanet is rotationg with speed of {rotationspeed}")



list=[1,2,3,46,6]
print(list.__class__)


mercury  = planet("mercury",800,2000)

venus=planet("venus",500,4000)

print("---------------------------------------------------")

print(mercury.radius)
mercury.revolve()
mercury.rotate(700)

venus.revolve()
venus.rotate(500)
print(mercury)
print(venus)

myList=["apple","mango","banana","watermelon","chillies",1,2,3,4,5,6]
print(myList)
print(len(myList))

numbersList=[6,7,8,9,3,4,5,6,77,88,444,11,0,12,67]
stringList=["apple","apple2","banana","watermelon","chillies"]


testList=[[12,3,4],[6,7,8],"stringtext"]
print(testList)



print(sum(numbersList))
print(min(numbersList))
print(max(stringList))
print(len(stringList))


print(stringList[4])

stringList[0]="orange"

stringList.append("apple")
stringList.insert(4,"test")
print(stringList[4])
print(stringList)
print(stringList.sort())
print(stringList)


mySet={2,4,5,7,8,9,9,8}
print(mySet)

mySet.add(77)
mySet.add(99)
mySet.remove(2)
print(mySet)
print(99 in mySet)

print(sum(mySet))
print(min(mySet))
print(max(mySet))
Strset={"apples","magos","chillies","oranges","Oranges"}
print(Strset)


myDict={1:"apples",2:"oranges",3:"chilies",4:"watermelon",4:"mangoes"}
print(myDict)
print(myDict[1])
del myDict[1]
print(myDict)
testDict={x:x+2 for x in range(0,10)}
print(testDict)


def revolve(inputs):
    print("test revolve func")

revolve("earth")

print("earth" + "myplanet") #concat
print(2  +  4) #numervial addition


y=mx+c