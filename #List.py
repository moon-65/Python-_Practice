#List 
Lucky_numbers=[32 , 43, 54,23 , 43]
friends=["shahid", "ali", "hamza", "zain"]

friends.extend(Lucky_numbers) #to extend the list
friends.append("Ahmed") #add at the end of the list
friends.insert(2, "Jamal") #custom add
friends.remove("Jamal") 
Lucky_numbers.clear()
friends.pop()# removes the last letter
print(friends)

print(friends.index("ali"))

# functions 

def hi(name):
    print("Hello "+ name)

hi("muaaz")
hi("ali")

def cube(num):
         return num*num*num

print (cube(4))


