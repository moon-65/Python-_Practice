sentence=("I'm currently in university sitting in hostel room and the room is too much hot")
words= sentence.split()
frequency={}
for word in words:
    if word in frequency :
        frequency [word]+=1
    else:
        frequency[word] =1
print(frequency)
    