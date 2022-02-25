import re
# print(dir(re))
from re import findall

'''
1. magic cmethod
2. class and static method
3. Abstractions
4. generators and iterators
5. Excetption handelling
'''



# greeting  = " hello world welcome to regular expression "
# print(re.findall("hello", greeting))


# greeting = " Hello hello world welcome to hello regular expression in python there ."
# print(re.findall("hello", greeting))                    # case sensitive
# print(re.findall("hello", greeting, re.IGNORECASE))     # ignore case
# print(re.findall("h", greeting, re.IGNORECASE))
# print(re.findall("he", greeting, re.IGNORECASE))

'''1) . (dot)---->  matched with any charecter except new line '''

# print(re.findall(r".", greeting))

# [' ', 'H', 'e', 'l', 'l', 'o', ' ', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'w', 'e', 'l', 'c', 'o', 'm',
# 'e', ' ', 't', 'o', ' ', 'h', 'e', 'l', 'l', 'o', ' ', 'r', 'e', 'g', 'u', 'l', 'a', 'r', ' ', 'e', 'x', 'p', 'r', 'e', 's',
# 's', 'i', 'o', 'n', ' ', 'i', 'n', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 't', 'h', 'e', 'r', 'e', ' ', '.']


# print(re.findall(r"h.", greeting))           # ['he', 'he', 'ho', 'he']

greeting = "hello world hi there , how are you h "
# print(re.findall(r"h.", greeting))        # ['he', 'hi', 'he', 'ho', 'h ']
# print(re.findall(r".h", greeting))          # [' h', 'th', ' h', ' h']

# print(re.findall(r"a.b", "acb"))              ['acb']
# print(re.findall(r"a.b", "a2b"))
# print(re.findall(r"a.b", "a@b"))
# print(re.findall(r"a.b", "a-b"))
# print(re.findall(r"a.b", "a b"))
# print(re.findall(r"a.b", "ab"))                 # []
# print(re.findall(r"a.b", "amnb"))               # []
# print(re.findall(r"a.b", "amb a4b a@b"))        # ['amb', 'a4b', 'a@b']

# print(re.findall(r"hello", "hello world hello world"))                # ['hello', 'hello']

'''2)  ^    ----> is used to get the first word from the sentence , which we input     
syntax is -->     " ^input "       
    it is  specify the pattern should be at the start of the string'''

# print(re.findall(r"^hello", "hello world hello world"))                # ['hello']

''' so it will throw empty list if the input char/ word is not the begining word or char of that sentence '''

# print(re.findall(r"^hello", " world hello world"))         #  []
# print(re.findall(r"hello", " world hello world"))          # ['hello']

'''3)    ' $  '  ----> specify the pattern should be at the end of the string '''

# print(re.findall(r"hello$", "hello world"))                  # []
# print(re.findall(r"hello$", "hello world hello"))            # ['hello']

# print(re.findall(r"a.a", "ana hello world axa"))               # ['ana', 'axa']

# print(re.findall(r"a..a", "anna"))                      # ['anna']
# print(re.findall(r"a..a", "annna"))                       # []

'''4)     '   *   '  --------------> will match the occurance of pre-charecter '0 or any number' of times '''

# print(re.findall(r"a.*a", "annna"))                         # ['annna']
# print(re.findall(r"an*a", "annnnnnnnnnnnna"))               # ['annnnnnnnnnnnna']
# print(re.findall(r"an*a", "aa"))                            # ['aa']
# print(re.findall(r"an*a", "annnnnnnnnnma"))                 # []
# print(re.findall(r"a.*a", "annnnnnnnnnma"))         # any charecter between tho char    ['annnnnnnnnnma']
# print(re.findall(r"a.*a", "annnnnannnnnma"))                # ['annnnnannnnnma']
# print(re.findall(r"a.*a", "a@@123165461,./l$%^ahdjdhja"))     # ['a@@123165461,./l$%^ahdjdhja']
# print(re.findall(r"an*a", "hello there ana"))                   # ['ana']
# print(re.findall(r"^an*a", "anna hello there ana"))           # ['anna']
# print(re.findall(r"^an*a", "ana hello there ana"))              #['ana']

# print(re.findall(r"^deb$", "deb"))                           # ['deb']
# print(re.findall(r"an*a", "a"))                               # []

'''5)   '    +    '   ------> will match the occurance of previous charecter '1 or more' number of times '''
# print(re.findall(r"an+a", "aa"))                   # []
# print(re.findall(r"an+a", "ana"))                  # ['ana']
# print(re.findall(r"an+a", "annnnnnnnna"))          # ['annnnnnnnna']


'''6) '    ?    '   ------> specify 0 nd 1 charecter present in betwwen that given charecter 
 will match the occurance of pre-charecter ' 0 or 1 'times   '''

# print(re.findall(r"an?a", "annnnnnnnna"))             # []
# print(re.findall(r"an?a", "ana"))                    # ['ana']
# print(re.findall(r"an?a", "aa"))                   # ['aa']
#
# print(re.findall(r"colou?r", "what colour do you like"))              # ['colour']
# print(re.findall(r"colou?r", "what color do you like"))               #['colour']
# print(re.findall(r"https?://", "https://www.google.com"))                 # ['https://']
# print(re.findall(r"https?://", "httpsss://www.google.com"))               # []

# print(re.findall(r"", "hello world welcome to python"))
     #['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']


# print(re.findall(r"[aeiou]", "hello world welcome to python"))     # ['e', 'o', 'o', 'e', 'o', 'e', 'o', 'o']
# print(re.findall(r"[helo]", "hello world"))          # ['h', 'e', 'l', 'l', 'o', 'o', 'l']

# print(re.findall(r"[abc]", "hello world and this is charecter is python "))     # ['a', 'c', 'a', 'c']

# print(re.findall(r"[0123456798]", "the cost of this book is $100"))            # ['1', '0', '0']
# print(re.findall(r"[0-9]", "the cost of this book is $100"))                   # ['1', '0', '0']

# print(re.findall(r"[0-9]", "the cost of this book is $568991"))                # ['5', '6', '8', '9', '9', '1']
# print(re.findall(r"[0-5]", "the cost of this book is $568991"))              # ['5', '1']
# print(re.findall(r"[a-z]", "THE cOst of thIS Book iS $568991"))      # ['c', 's', 't', 'o', 'f', 't', 'h', 'o', 'o', 'k', 'i']


'''7) [0123465798] ======  [0-9] ======" \d "
[0-5] ==== 013245 ======== 
[0-9]+ or \d+   $568991 and the cost is $ 5623-------> ['568991', '5623']
[0-9]      -----------> ['5', '6', '1', '5', '6', '2', '3']
'''
# print(re.findall(r"[0-9]+", "THE cOst of thIS Book iS $568991"))         #  ['568991']
# print(re.findall(r"[0-9]+", "THE cOst of thIS Book iS $568991 and the cost is $ 5623"))         # ['568991', '5623']
# print(re.findall(r"[0-9]", "THE cOst of thIS Book iS $561 and the cost is $ 5623"))  # ['5', '6', '1', '5', '6', '2', '3']

# print(re.findall(r"\d+", "THE cOst of thIS Book iS $568991 and the cost is $ 5623"))   # ['568991', '5623']
# print(re.findall(r"\d", "THE cOst of thIS Book iS $568991 and the cost is $ 5623")) # ['5', '6', '8', '9', '9', '1', '5', '6', '2', '3']


'''8) want to match everything but not numbers -------->  [^0-9]'''
# print(re.findall(r"[^0-9]", "THE cOst of thIS Book iS $561 and the cost is $ 5623"))
#
# #['T', 'H', 'E', ' ', 'c', 'O', 's', 't', ' ', 'o', 'f', ' ', 't', 'h', 'I', 'S', ' ',
# # 'B', 'o', 'o', 'k', ' ', 'i', 'S', ' ', '$', ' ', 'a', 'n', 'd', ' ', 't', 'h', 'e', ' ',
# # 'c', 'o', 's', 't', ' ', 'i', 's', ' ', '$', ' ']

# print(re.findall(r"[^0-5]", "THE cOst of thIS Book iS $5691 and the cost is $ 5623"))
## ['T', 'H', 'E', ' ', 'c', 'O', 's', 't', ' ', 'o', 'f', ' ', 't', 'h', 'I', 'S', ' ', 'B', 'o', 'o', 'k', ' ', 'i', 'S',
##' ', '$', '6', '9', ' ', 'a', 'n', 'd', ' ', 't', 'h', 'e', ' ', 'c', 'o', 's', 't', ' ', 'i', 's', ' ', '$', ' ', '6']


# print(re.findall(r"[^0-5]+", "the cost is $250"))              # ['the cost is $']
# print(re.findall(r"[^\d]", "the cost is $250"))  # ['t', 'h', 'e', ' ', 'c', 'o', 's', 't', ' ', 'i', 's', ' ', '$']
# print(re.findall(r"[^\d]+", "the cost is $250"))      # ['the cost is $']

'''9) it avoid space and special charecters ---------> [A-Za-z0-9] --------> \w  
     [^A-Za-z0-9]---------> \W'''

# print(re.findall(r"[A-Za-z0-9]", "THE cOst of thIS Book iS $568991 and the cost is $ 5623"))
# #['T', 'H', 'E', 'c', 'O', 's', 't', 'o', 'f', 't', 'h', 'I', 'S', 'B', 'o', 'o', 'k', 'i', 'S', '5', '6', '8', '9',
# # '9', '1', 'a', 'n', 'd', 't', 'h', 'e', 'c', 'o', 's', 't', 'i', 's', '5', '6', '2', '3']

# print(re.findall(r"[A-Za-z0-9]+", "THE cOst of thIS Book iS $568991 and the cost is $ 5623"))
# # ['THE', 'cOst', 'of', 'thIS', 'Book', 'iS', '568991', 'and', 'the', 'cost', 'is', '5623']

# print(re.findall(r"\w", "THE cOst of thIS Book iS $568991 and the cost is $ 5623"))
# #['T', 'H', 'E', 'c', 'O', 's', 't', 'o', 'f', 't', 'h', 'I', 'S', 'B', 'o', 'o', 'k', 'i', 'S',
# # '5', '6', '8', '9', '9', '1', 'a', 'n', 'd', 't', 'h', 'e', 'c', 'o', 's', 't', 'i', 's', '5', '6', '2', '3']


# print(re.findall(r"\W", "THE cOst of thIS Book iS $568991 and the cost is $ 5623"))
# #[' ', ' ', ' ', ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ', ' ', '$', ' ']


''' 10)  \d ------> matches all digits from 1 to 9
         \D ------> matches everything apart from digits  == [^0-9] '''
# print(re.findall(r"\d", "THE cOst of thIS Book iS $568991 and the cost is $ 5623"))
# #['5', '6', '8', '9', '9', '1', '5', '6', '2', '3']

# print(re.findall(r"\D", "THE cOst of thIS Book iS $568991 and the cost is $ 5623"))
# #['T', 'H', 'E', ' ', 'c', 'O', 's', 't', ' ', 'o', 'f', ' ', 't', 'h', 'I', 'S', ' ', 'B', 'o', 'o', 'k', ' ',
# # 'i', 'S', ' ', '$', ' ', 'a', 'n', 'd', ' ', 't', 'h', 'e', ' ', 'c', 'o', 's', 't', ' ', 'i', 's', ' ', '$', ' ']


''' 11)  \s --------> matches with white space '''
# print(re.findall(r"\s", "THE cOst of thIS Book iS $568991 and the cost is $ 5623"))
# #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# print(len(re.findall(r"\s", "THE cOst of thIS Book iS $568991 and the cost is $ 5623")))      # 12

# print(re.findall(r"\S", "THE cOst of thIS Book iS $568991 and the cost is $ 5623"))
#['T', 'H', 'E', 'c', 'O', 's', 't', 'o', 'f', 't', 'h', 'I', 'S', 'B', 'o', 'o', 'k', 'i', 'S', '$', '5',
# '6', '8', '9', '9', '1', 'a', 'n', 'd', 't', 'h', 'e', 'c', 'o', 's', 't', 'i', 's', '$', '5', '6', '2', '3']


# print(len(re.findall(r"\S", "THE cOst of thIS Book iS $568991 and the cost is $ 5623")))     # 43






# sentence = "the pincode of bangalore is 560001 and the telephone code is 080 ph: 7978423230"
# print(re.findall(r"\d+", sentence))                              # ['560001', '080']
# print(re.findall(r"\d\d\d\d\d\d", sentence))           # 6 contineous digit ['560001']
# print(re.findall(r"\d{6}", sentence))              # ['560001']

# print(re.findall(r"\d{6}", sentence))            # ['560001', '797842']

'''12)    \b  ----------> transaction between non-word charecter to word-charecter and vice-versa   '''
# print(re.findall(r"\b\d{6}\b", sentence))
# word = "i am travelling from BLR to DLH in JULY"
# print(re.findall(r"\b[A-Z]{3}\b", word))            # ['BLR', 'DLH']

# word = "i am travelling from BLR to DLH in JUL+Y"
# print(re.findall(r"\b[A-Z]{3}\b", word))                   # ['BLR', 'DLH', 'JUL']


# print(re.findall(r"\w{2}", "hi hello"))         # ['hi', 'he', 'll']
# print(re.findall(r"\w{2,5}", "hi hello and python is a programming language"))
# #['hi', 'hello', 'and', 'pytho', 'is', 'progr', 'ammin', 'langu', 'age']

# print(re.findall(r"\b\w{2,5}\b", "hi hello and python is a programming language"))    # ['hi', 'hello', 'and', 'is']

sentence = "hello hi world hello how are you h How"

# print(re.findall(r"\bh\w+", sentence))               # ['hello', 'hi', 'hello', 'how']
# print(re.findall(r"\bh\w+\b", sentence))

# print(re.findall(r"\bh\w*\b", sentence))             # ['hello', 'hi', 'hello', 'how', 'h']
# print(re.findall(r"\bh\w*
# print(re.findall(r"\bh\w*", sentence, re.IGNORECASE))          # ['hello', 'hi', 'hello', 'how', 'h', 'How']
# print(re.findall(r"\bh\w+", sentence, re.IGNORECASE))            #['hello', 'hi', 'hello', 'how', 'How']


''' the words which ends with y or o '''

# print(re.findall(r"\b\w+o\b", sentence))                    # ['hello', 'hello']
# word = "Sony12India pvt34 Ltd567 Bangalore "
# # 1 + 2 + 3 + 4 + 5 + 6 + 7
# # 12 + 34 + 567
#
# number = re.findall(r"\d", word)
# print(number)                                 # ['1', '2', '3', '4', '5', '6', '7']
# total = 0
# for item in  number:
#     total += int(item)
#
# print(total)                                   # 28




# word = "Sony12India pvt34 Ltd567 Bangalore "
# # 1 + 2 + 3 + 4 + 5 + 6 + 7
# # 12 + 34 + 567
#
# number = re.findall(r"\d+", word)
# print(number)                 # ['12', '34', '567']
# total = 0
# for item in  number:
#     total += int(item)
#
# print(total)                        # 613


# sentence = "the pincode of bangalore is 560001 and the telephone code is 080 ph: 7978423230"
# space = re.findall(r"\s", sentence)
# print(len(space))                      # 13




''' wap to count the number of charecter occurance of each non special charecters '''

# letters = re.findall(r"\w", sentence)
# print(letters)
# # ['h', 'e', 'l', 'l', 'o', 'h', 'i', 'w', 'o', 'r', 'l', 'd', 'h', 'e', 'l', 'l',
#  # 'o', 'h', 'o', 'w', 'a', 'r', 'e', 'y', 'o', 'u', 'h', 'H', 'o', 'w']
#
# count ={c: letters.count(c) for c in letters}
# print(count)        # {'h': 5, 'e': 3, 'l': 5, 'o': 6, 'i': 1, 'w': 3, 'r': 2, 'd': 1, 'a': 1, 'y': 1, 'u': 1, 'H': 1}


''' filterout only those charetcers accept digits'''

# word = "@hello12world34welcome!123"
# c = re.findall(r"\D", word)  # ['@', 'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'w', 'e', 'l', 'c', 'o', 'm', 'e', '!']
#
# s = ''.join(c)
# print(s)             # @helloworldwelcome!


# sentence = "Hi there! How are you:) How are you doing today"

# print(re.findall(r"\w+", sentence))
# print(re.findall(r"\b\w+\b", sentence))  # ['Hi', 'there', 'How', 'are', 'you', 'How', 'are', 'you', 'doing', 'today']
# word = re.findall(r"[a-zA-Z0-9]+", sentence)
# print({words: len(words) for words in word})  # {'Hi': 2, 'there': 5, 'How': 3, 'are': 3, 'you': 3, 'doing': 5, 'today': 5}



'''count the number of lower case and upper case charecter '''

# sentence = "Hello Word Welcome To Python"
# upper_count = len(re.findall(r"[A-Z]", sentence))
# print(upper_count)              # 5
# lower_count = len(re.findall(r"[a-z]", sentence))
# print(lower_count)              # 19




download_message = '''
Downloading file archive.zip to downloads folder...
Downloading file image.jpeg to downloads folder...
Downloading file index.xhtml to downloads folder...
Downloading file python.py to downloads folder...
'''

# message = re.findall(r"\.[a-zA-Z]+", download_message)
# print(message)                 # ['.zip', '.jpeg', '.xhtml', '.py']

# file_format = ['Graphics Interchange Format',
#                'Advance Audio Coding',
#                'Comma Separated Value'
#                ]
#
# for item in file_format:
#     match = re.findall(r"[A-Z]", item)
    # print(''.join(match))               # GIF
    #                                       AAC
    #                                       CSV


# phone_number = ['123-456-0789', '456-9832-098', '800-987-1234', '080-78946512']
#
# for item in phone_number :
#     match = re.findall(r'\d{3}-\d{3}-\d{4}', item)
#     if match :
#         print(match)
#     else:
#         print(f"the number {item} is invalid")
#     # output
# # ['123-456-0789']
# # the number 456-9832-098 is invalid
# # ['800-987-1234']
# # the number 080-78946512 is invalid


# phone_number = ['123-456-0789', '456-9832-098', '800-987-1234', '810-78946512', '900-898-5656']
#
# for item in phone_number:
#     match = re.findall(r'[89]00-\d{3}-\d{4}', item)
#     print(match)
#output
    # []
    # []
    # ['800-987-1234']
    # []
    # ['900-898-5656']



''' print only tjose words which sgtarts with vowel charecters '''

# sentence = " hello hi american engineers and indian writers officers united states"
# match = re.findall(r'\b[aeiou]\w+', sentence)
# print(match)                                      # ['american', 'engineers', 'and', 'indian', 'officers', 'united']


# match = re.findall(r'\b[^aeiou\s]\w+', sentence)
# print(match)                       # ['hello', 'hi', 'writers', 'states']



# sentence = " hello hi how are you what is your name he is older then me how old are you "
#
# match = re.findall(r'\b\w{3}\b', sentence)
# print(match)               # ['how', 'are', 'you', 'how', 'old', 'are', 'you']
# print(len(match))          # 7