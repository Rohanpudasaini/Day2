# 17. Write a Python program to find if a given string starts with a given character using Lambda. 
check_char = "r"
string_to_check = "Ganesh"
check = lambda x: x.startswith(check_char.lower()) or x.startswith(check_char.upper())
print(check(string_to_check))
# print((filter(lambda x: x == check_char, string_to_check[0])))