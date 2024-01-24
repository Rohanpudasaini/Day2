# 6. Write a Python function to check whether a number is in a given range. 

# higher = int(input("Enter the higher range: "))
# lower =  int(input("Enter the lower range: "))
# num =  float(input("Enter the number to ceck: "))
higher = 10
lower = 0
num = 12

def is_between(higher:int, lower:int, num:float) -> bool:
    if num < higher and num > lower:
        return True
    return False

print(is_between(higher, lower, num))