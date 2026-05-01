# for loop
for letter in 'Python':
    print(letter) 

friends = ['John', 'Jane', 'Doe']
for friend in friends:    
    print(friend) 


for index in range(len(friends)):
    print(index, friends[index])

for index in range(5):
    if index ==0:
        print('First iteration')
    else:
        print('Not first iteration')

def rise_to_power(base, pow):
    result =1
    for index in range (pow):
        result = result * base
    return result
print(rise_to_power(2,3))

# 2D list
no_of_grids = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[0]]
# print rows
for row in no_of_grids:
    print(row)
# print columns
for row in no_of_grids:
    for col  in row:
        print(col)