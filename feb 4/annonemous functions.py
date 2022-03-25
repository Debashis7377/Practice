'''square of a number '''

# #normal method
# def square(num):
#     return num ** 2
# print(square(2))

''' last element of sequence'''
# res = lambda seq: seq[-1]
# print(res("debashis"))
#print(res)

''' wa lambda function that checks if the given string is palindrome or not '''

# res= lambda st:st == st[::-1]
# print(res("mom"))

# res = lambda st: st if st == st[::-1] else "not a palindrome"
# print(res("deba"))
# res = lambda st: f"{st}is a palindrome" if st == st[::-1] else "not a palindrome"


''' wap that checks whether the number is even or odd and print the number in both the cases '''

# res = lambda num: "num is even" if num % 2 == 0 else "odd"
# print(res(21))

''' wap that checks if the given list of numbers are even or odd '''
# list_ = [10,20,65,89,78]
# res = lambda item: f"{item} is even" if item % 2 == 0 else f"{item} is odd"
# print(list(map(res, list_)))
# print(list(map(lambda item: f"{item} is even" if item % 2 == 0 else f"{item} is odd", list_)))

''' wap to return the strings which are starting with vowels '''
st = ['apple','gmail','yahoo','flipcart']
# print(list(map((lambda item:f"{item} is a vowel" if item[0].lower() in "aeiou" else f"{item} not start with vowel"),st)))
# res = lambda item: f"{item} is a vowel" if item[0].lower() in "aeiou" else f"{item} is not a vowel"
# out = list(map(res,st))
# print(out)


# def vowel(item):
#     if item.lower() in "aeiou":
#         return item
# res = map(vowel, st)
# print(list(res))

# sentence = "python is a language, python programming is easy"
# words = sentence.split()
#
# dd = {index: word if len(word) % 2 == 0 else  word[::-1] for index, word in enumerate(words)}
# print(dd)


'''  ||   most important  ||  '''

''' Note -- > in lambda function we can give multiple variable ( collections as their arguments),
 but we cant give multiple expressions '''


