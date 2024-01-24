# 1. Write a Python function to find the Max of three numbers. 
import math

number = (input("Enter 3 numbers seperated by ',': ")).split(",")
max = -math.inf
for num in number:
    try:
        num = int(num)
    except TypeError:
        print("Given input isnt a number")
        exit(0)
    if num > max:
        max = num
print(f"Max number is {max}")
