#translator
def translator(phrase):
    phrase = phrase.upper()
    translation =""
    for letter in phrase:
        if letter in "A":
            translation = translation + "."
        elif letter in "B":
            translation = translation +">"
        elif letter in "C":
            translation = translation + "<"
        elif letter in "D":            
            translation = translation + "[)"
        elif letter in "E":                         
            translation= translation+ "@"
        elif letter in "F":
            translation = translation + "7"
        elif letter in "G":
            translation = translation + "6"
        elif letter in "H":
            translation = translation + "#"
        elif letter in "I":
            translation = translation + "!"
        elif letter in "J":
            translation = translation + "]"
        elif letter in "K":
            translation = translation + "<"
        elif letter in "L":
            translation = translation + "1"
        elif letter in "M":
            translation = translation + "^^"
        elif letter in "N":
            translation = translation + "^/"
        elif letter in "O":
            translation = translation + "0"
        elif letter in "P":
            translation = translation + "|D"
        elif letter in "Q":
            translation = translation + "(,)"
        elif letter in "R":
            translation = translation + "|Z"
        elif letter in "S":
            translation = translation + "$"
        elif letter in "T":
            translation = translation + "+"
        elif letter in "U":
            translation = translation + "|_|" 
        elif letter in "V": 
            translation =translation +":" 
        elif letter in "W": 
            translation=translation+"*&" 
        elif letter in "X":  
            translation=translation+"}{"
        elif letter in "Y":
            translation=translation+"`/"
        elif letter in "Z":
            translation=translation+"2"
        else:           
            translation = translation + letter
    return translation      
print(translator(input("Enter a phrase: ")))    