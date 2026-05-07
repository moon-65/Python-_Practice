num= int (input("Enter a number: "))
if num < 2:
    print("Not a prime number ")
else:
       is_prime = True
for i in range(2, num):
    if num % i ==0:
        is_prime = False
        break

if is_prime== True:
   print ("Entered number is prime")
else:
    print ("Entered number is not prime")
 

