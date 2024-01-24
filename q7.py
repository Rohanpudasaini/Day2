# 7. Write a Python function that accepts a string and calculate the number of 
# upper case letters and lower case letters. 
# Sample String : 'The quick Brow Fox' 
# Expected Output : 
# No. of Upper case characters : 3 
# No. of Lower case Characters : 12 

sample_string = 'The Quick Brow Fox'

def get_count(string:str) -> str:
    upper, lower = 0, 0
    for chr in string:
        if chr.isupper():
            upper+=1
        if chr.islower():
            lower+=1
    return(f'No. of Upper case characters: {upper}\nNo. of Upper case characters: {lower} ')

print(get_count(sample_string))
