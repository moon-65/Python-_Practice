print("Guess the Word")
word ="Dog"
guess= " "
guess_count= 0
guess_limit = 3
while guess != word and guess_count< guess_limit:
     guess= input("Enter the word (Hint: word is the name of a street animal starting with 'D' )")
     guess_count +=1

if guess == word:
    print ("You Win!!!!")
else:    
 print("out of guesses, You lose!!")
    