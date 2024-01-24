# 18. Write a Python program to check whether a given string is number or not using Lambda. 

string = "½"
check = lambda x : x.isnumeric()
print(check(string))