'''create a dictionary of charecter and its count '''

# d1={char : s.count(char) for  cahr in s}



'''create a dictionary of words and its count'''
# s="python "
# #normal method


'''wap to create a dictionary of word and its count/ length pair only if the words is of even length'''

# sentence = "python is a language , python programming is easy"
# words = sentence.split()

# #normal method
# for word in words:
#     if len(word) % 2 == 0 :
#         d[word] = words.count(word)
# print(d)

# comprehension method

# dd= {word : words.count(word) for word in words if len(word) % 2 == 0 }
# print(dd)

'''dictionary with index and word pair if the word is of odd length or keep it as it is '''

# sentence = "python is a language , python programming is easy"
# words = sentence.split()
# d={}
# # for index,word in enumerate(words) :
# #     if len(word) % 2 == 0:
# #         d[word] = word
# #     else:
# #         d[index] = word[::-1]
# # print(d)
#
# # comprehension method
#
# dd={index: word if len(word) % 2 == 0 else word[::-1] for index,word in enumerate(word)}
# print(dd)

'''wap to create a dictionary word with its length pair only if the word is starting with the vowel '''

# sentence = "python is a language , eython programming is easy"
# words = sentence.split()
# d = {word: len(word) for word in words if word[0].lower() in "aeiou"}
# print(d)

'''index and its word pair if word is of type string reverse it'''

# list_ = ["python",17,9,'java',19.9,4+8j,'rubby','c++']

# d={index:item[::-1]if isinstance(item,str) else item for index, item in enumerate(list_)}
# print(d)

'''wap to creat a ditionary with index and word pair , if is of type string keep it as it is else reverse it '''
# list_ = ["python",17,9,'java',19.9,4+8j,'rubby','c++']
#
# # d1 = {index:item if isinstance(item,str) else str(item)[::-1] for index,item in enumerate(list_)}
# d1 = {index: str(item)[::-1] if not isinstance(item,str) else item for index,item in enumerate(list_)}
# print(d1)

'''flip keys and values in a dictionary'''
# dict_ = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# res = {dict_[key]:key for key in dict_}
# print(res)
#
# res = {value: key for key, value in dict_.items()}
# print(res)

'''wap to creat a dictionary of charecter and its ascii value pair'''
# string = "python"
#
# res = {item: ord(item) for item in string}
# print(res)

"""practice"""

'''wap to create a dictionary , word and its count only if the word is not repeated '''

# sentence = 'python is a language, python programming is easy '
# list_ = sentence.split()
# d = {}
# for item in list_:
#     d[item] = list_.count(item)
# print(d)


# res = {item: list_.count(item) for item in list_ if list_.count(item) > 1 }
# print(res)


''' program'''
a = "hello world hi welcome monkey"
r = a.split()
# print(r)
d = {}
for i in r:
    if i[0] not in d:
        d[i[0]] = [i]
    else:
        d[i[0]] += [i]
print(d)
