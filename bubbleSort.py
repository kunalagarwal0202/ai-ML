def bubble_sort(arr):
    n = len(arr)
    print(n)

    for i in range(n):
        # Last i elements are already sorted
        print(f"the value of i is {i}")
        print(arr)
        for j in range(0, n-1):
            print(f"the value of j is {j}")
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
[9,8,7,6,5,4,3,2,1]
sorted_numbers = bubble_sort(numbers)

print("Sorted array:", sorted_numbers)