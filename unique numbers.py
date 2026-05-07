number=(1,2,3,5,3,6,3,5,8,9,4,7,9,5,4,3,2)
unique=[]
for item in number:
    if item not in unique:
        unique.append(item)
print("The orignal list is:")
print(number)
print("Unique numbers in the list are:")
print(unique)
