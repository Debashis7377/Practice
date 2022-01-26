char = input("enter the string")
if char[0] in "aeiouAEIOU":

    print({char[0]: ord(char[0])})
else:
    print("CONSONANT")



# thi is another method

# 1
# d={}
# d[char]= ord(char)

#2
# d.update({char:ord(char)})

#3
# d.setdefault(char,ord(chr))

