text= input("Enter a sentence: ")
vowel= "aeiouAEIOU"
count =0
for char in text:
   if char in vowel:
       count+=1
print ("Number of vowel in the sentence is: ", count)