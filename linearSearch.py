#recursion
def funtest():
    print("this is my test recursion")
    #funtest()

funtest()



list=[1,20,3,4,566,6,667,338,9,-10]

def linearSearch(list, key):
    length=len(list)
    for i in range(0,length):
        if key==list[i]:
            print(f"found the elemenet{key} at index{i}")



linearSearch(list,10)

def factorial(num):
    if(num==0 or num==1):
        return 1
    return num*factorial(num-1)

print(factorial(5))

testlist=[0,1,2,3,4,5,6,7,8,9]
def binarySearch(testList,key):
    length=len(testList)
    low=0
    high=length-1
    while low<=high:
        mid=((low+high)//2)
        if testList[mid]==key:
            print(f"found the elemenet{key} at index{mid}")
            return mid
        elif testList[mid]>key:
            high=mid-1
        elif testList[mid]<key:
            low=mid+1
        else:
            return -1


print(binarySearch(testlist,8))