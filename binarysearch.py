#Binary search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1



arr = [5,6,9,11,56,100,999]
x = 11

result = binary_search(arr, x)

if result != -1:
    print("Element is present")
else:
    print("Element is not present in array")
