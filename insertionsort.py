#Insertion sort


def isort(list):
   for i in range(1, len(list)):
      a = list[i]
      j = i-1
      while j >=0 and a < list[j] :
         list[j+1] =list[j]
         j =j- 1
      list[j+1] = a

list=[33,94,21,6,11,7,0,8]
isort(list)
print(list)
