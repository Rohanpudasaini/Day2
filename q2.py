# 2. Write a Python function to sum1 all the numbers in a list. 
# Sample List : (8, 2, 3, 0, 7) 
# Expected Output : 20 

sample_list = [8,2,3,0,7]
def sum1_list(sample_list:list) ->int:
    sum1 = 0
    for num in sample_list:
        sum1 +=num
    return sum1

print(sum1_list(sample_list))