# 3. Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7) 
# Expected Output : -336 

sample_list = [8, 2, 3, -1, 7]
def mul_list(sample_list:list)->int:
    mul = 1
    for num in sample_list:
        mul *=num
    return mul

print(mul_list(sample_list))

    
