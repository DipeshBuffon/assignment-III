#Bubble sort

def bsort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

list=[33,94,21,6,11,7,0,8]
bsort(list)
print(list)
