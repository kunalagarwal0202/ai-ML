def linearSearch(myList, value):
    isFound=False

    for i in range(0,len(myList)) :
        if(myList[i]==value):
            print(f"i value { i}")
            print(f"current list value {myList[i]}")
            print(f"We have found the element at the index{i}")
            isFound=True
            break
    if(not isFound):   

        print("element not found")

test_list=[66,77,88,99,5,2,3,4,5,6,7,89,102, 30, 60, 50, 40, 45, 76]
linearSearch(test_list, 76)


def binary_search(myList, value):
    lower_index=0

    high_index=len(myList)-1
    i=0
    while (lower_index<=high_index):
        mid_index=(lower_index+high_index)//2
        print(i)
        i=i+1
        print(f"lowerindex{lower_index}")
        print(f"higher index{high_index}")
        print(f"mid index{mid_index}")
        print(f"my list curetn mid value{myList[mid_index]}")
        if(myList[mid_index]==value):
            print(f"found the value at index with binary search { mid_index}")
            return mid_index
        elif(myList[mid_index]<value):
            lower_index=mid_index+1
        else:
            high_index=mid_index-1
    return -1




myList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
index=binary_search(myList, 2)
if(index==-1):
    print("elemenat not found from binary search")




    