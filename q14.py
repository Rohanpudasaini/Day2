# 14. Write a Python program to sort a list of dictionaries using Lambda. 
dict1 = {9: 2, 6: 4, 1: 6, 4: 8, 5: 10}
# print(sorted(dict1.items(), key=lambda x: x[0]))

print(dict(sorted(dict1.items(), key= lambda x: x[0])))
