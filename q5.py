# 5. Write a Python function to calculate the factorial of a number (a non-negative 
# integer). The function accepts the number as an argument.
def get_fact(num:int) -> int:
    fact = 1
    if num == 0:
        return fact
    for i in range(1,num+1):
        fact *=i
    return fact

print(get_fact(4))