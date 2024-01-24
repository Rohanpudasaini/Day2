# 16. Write a Python program to square and cube every number in a given list of 
# integers using Lambda. 
list1 =[6,1,3,5, 15,12]
print(list1)
print(list(map(lambda x:x**2, list1)))
print(list(map(lambda x:x**3, list1)))
