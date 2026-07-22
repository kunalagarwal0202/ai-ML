def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 0, len(arr)-1, 7))




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



def power(base, exp):
    if exp == 0:
        return 1

    return base * power(base, exp - 1)

print(power(2, 5))


base = 2
exp = 5
result = 1

for _ in range(exp):
    result *= base

print(result)


def sum_n(n):
    if n == 1:
        return 1

    return n + sum_n(n - 1)

print(sum_n(5))

n = 5
total = 0

for i in range(1, n + 1):
    total += i

print(total)


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")


n = 10
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))