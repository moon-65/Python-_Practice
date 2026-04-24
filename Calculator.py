num_1= float(input("Input the First Number"))
num_2=float( input ("Enter the second Number "))
opr= input("Enter the operation you what to perform(+,-,*,/)")
add= (num_1 + num_2)
sub= (num_1 - num_2)
multi= (num_1 * num_2)
divide= ( num_1 / num_2)

if opr== '+':
  print(add)
elif opr== '-':
   print(sub)
elif opr=='*':
   print(multi)
elif opr=='/':
    print(divide)
else :
   print("Incorrect Function")