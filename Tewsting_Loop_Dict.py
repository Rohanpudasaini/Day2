dict1 = {"name":"Rohan",
         "Laptop": "HP",
         "Drink": "Tea"}

dict2 = {"surname": "pudasaini",
         "address": "Kathmandu",
         "name": "Ganesh"}


for key, value in dict2.items():
    # if key not in dict1:
    dict1[key] = value
    
print(dict1)

# d3 = {x:x*x for x in range(1,5)}

string1 = ("hello")

