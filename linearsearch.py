#Linear search

def search(arr, x):

    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1

print(search([9,11,5,3,6],3))
