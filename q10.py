# 10. Write a Python program to print the even numbers from a given list. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Expected Result : [2, 4, 6, 8] 

sample_list = [1, 2, 10, 4, 5, 6, 7, 8, 9]

print([x for x in sample_list if x%2==0])
# new_sample_list = sample_list[1::2]
# print(new_sample_list)
