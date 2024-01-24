# 13. Write a Python program to sort a list of tuples using Lambda. 
tupl1 = (6,4,3,1,7)
sorted1 = lambda x: sorted(list(x))
print(tuple(sorted1(tupl1)))