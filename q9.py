# 9. Write a Python function that takes a number as a parameter and check the 
# number is prime or not. 
# Note : A prime number (or a prime) is a natural number greater than 1 and that 
# has no positive divisors other than 1 and itself. 

def is_prime(num:int)->bool:
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(is_prime(137))
