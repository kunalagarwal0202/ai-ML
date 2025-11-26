import numpy as np

n= np.array((1,2,3,4,5,6))
print(n)

x= np.array(["123456789","123456789"], dtype='S12')
print(x.dtype)
print(x)

dim=np.array([[1,2,3,4],[5,6,7,8]])
print(dim[1,2])


test= np.array( [[ [1,2,4],[5,7,8]],  [[10,20,30],[50,60,70]]])
print(test[-1,-2,-1])

import numpy as np

arr= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
newArr= np.insert(arr,3,[[10,111,0]],axis=1)
print(newArr)
print (newArr[1][1])

newArr[1][1]=1000
print(newArr)
myList=[1,2,3,4,5,6,[89,00,88]]
print(myList)
for i in myList:
    print(i)
print(myList[6])
print(myList.index(2))
myList.insert(1,4)
myList.append(140)
myList.extend([1,2,3])
print(myList)
testList=myList[0:7]
testList.pop()
print(testList)
del testList[0]
testList.remove(2)
print(testList)

print(enumerate(myList))

a="testing0 testing1 testing3"
print(a.split("g"))
print(a)
str=list(a)
print(str)
print(a.join(str))

print(str)

test=[-1,3,-8,9,7,4]
exitList=[i*i for i in test if i<0]
print(exitList)

myarray= np.array([1,2,3,5,8,9,7])
for i in myarray:
    print(i)
def mypair(arr,val):
    ans=False
    for i in arr:
        for j in arr:
            if(i+j==val):
                ans= True
                break
    return ans
print(mypair(myarray,1))


def optiFun(arr, val):

    newMap={}
    for i,vali in enumerate(arr):
        print(i, vali)
        comp=val-vali
        if(comp in newMap):
            print(comp , " found")
        newMap[vali]=i
        print(newMap)
optiFun(myarray,9)


def twoPointer(arr, target):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<right):
        sum= arr[left]+arr[right]
        if(sum==target):
            print("found")
        elif(sum>target):
            left =left+1
        else:
            right =right+1

def freqMap(test):
    freMap= [0]*26

    for i in test:
        freMap[ord(i)-ord("a")] +=1
    
def reverse_dict(my_dict):
    new_dt=dict()
    for key, value in my_dict.items():
        new_dt[value]=key
    return new_dt

print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))

newTuple=('a','b')
print(type(newTuple))

class test:
    myvalue=1
    testvalue=3

test1= test()
print(test1.myvalue)
test1.myvalue=0
print(test.myvalue)