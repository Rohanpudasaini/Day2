# 11. Write a Python program to create a lambda function that adds 15 to a given 
# number passed in as an argument, also create a lambda function that multiplies 
# argument x with argument y and print the result. 

add_15 = lambda x: x+15
mult = lambda x,y: x*y
print(add_15(2))
print(mult(2,3))