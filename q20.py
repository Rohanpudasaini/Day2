# 20. Write a Python program to find intersection of two given arrays using Lambda. 
list1 = set([1,2,3,4,5])
list2 = set([3,4,5,8,7])
new = lambda x,y: list(x.intersection(y))
print(new(list1, list2)) 