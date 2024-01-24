# 8. Write a Python function that takes a list and returns a new list with unique 
# elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5] 
# Unique List : [1, 2, 3, 4, 5]

def get_unique(sample_list:list) -> list:
    uniqu_list = []
    for item in sample_list:
        if item not in uniqu_list:
            uniqu_list.append(item)
    return uniqu_list

sampl_list = [1,2,3,3,3,3,4,5,6,8]
print(get_unique(sampl_list))

