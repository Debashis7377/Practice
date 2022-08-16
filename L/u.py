# # # wap to check if the charecter is lower case or upper case
# char= input("enter the charecter ")
# # if "a" <=char <= 'z' :
# #     print(f"{char} is in lower case ")
# # else :
# #     if "A" <= char <= "Z" :
# #         print(f"{char} is in upper case ")
# #     else :
# #         print(f"{char} is not an alphababet")
#
#
# if "a" <=char <= 'z' :
#     print(f"{char} is in lower case ")
# elif "A" <= char <= "Z" :
#     print(f"{char} is in upper case ")
# else :
#     print(f"{char} is not an alphababet")
import csv
import json
import pickle

path = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\txt_log_files\sample.txt"
'''   1.      '''
# with open(path) as file:
# #     print(file.readline())
# #     file.seek(0)
# #     print(file.tell())
#
# # with open(path, "a") as file:
# #     file.writelines((["hi how are you ", "hello", "hiiiii", "janini"]))
#



''' 2.         '''
path1 = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\csv_files\employees.csv"
# with open(path1) as file:
#     ele = csv.reader(file)
#     print(ele)
#     for row in ele:
#         print(row)


# import csv
# with open(path1) as file:
#     ele = csv.DictReader(file)
#     print(ele)
#     for row in ele:
#         print(row)

#b
'''3.  '''
# import json
# a = {"hey": 3, "hello":4}
# b = json.dumps(a)
# print(b)
# print(type(b))

# import json
# asd = {"p":5,"q":6, "r":7 }
# with open("example.json", "a") as file:
#     print(json.dump(asd.file))
#
# b = json.dumps(asd)
# print(b)
'''4.   '''
# eid = {1: "deba", 2:"ashis"}
# with open("zero.pkl", wb) as file:
#     dumps():pickle.dumps(eid)


'''5.   '''
# with open(path) as file:
#     res = ""
#     count = 0
#     for line in file:
#         s = line.split()
#         print(s)
#         for word in s:
#             count+=1
#             if word == "python":
#
#                 res += 'c'
#             else:
#                 res += word
# print(res)
# print(count)











'''Write program to read a random line in a file. (ex. 50, 65, 78th line) '''
# def read_random_line(lineno):
#     f = open(path)
#     for index, line in enumerate(f, start=1):
#         if index == lineno:
#             return line
# print(read_random_line(5))




path2 = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\txt_log_files\access-log.txt"

# from itertools import islice
# def read_n_lines(start_line, end_line):
#     with open(path2) as f:
#         s = islice(f, start_line,end_line)
#         for line in s:
#             print(line)
#
# read_n_lines(10, 15)



# def read_n_lines(start_line, end_line):
#     with open('Data/access-log.txt') as enumerate(f, start=1):
#         if index in range(start_line, end_line):
#            print(index)
#
# read_n_lines(10, 15)





# from itertools import islice
# def last_n_lines(n):
#     line_count = 0
#     with open(path) as f:
#       for line in f:
#          line_count += 1
#       f.seek(0)
#       lines = islice(f, line_count-n, None)
#       return list(lines)
#
# print(last_n_lines(2))


# from collections import deque
# def tail(n):
#     with open(path) as f:
#         d = deque(f, n)             # only last 'n' lines will be loaded to the deque
#         return d
#
# print(tail(2))









# sentence = "hello world welcome to python programming hi there"
# # d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
# from collections import defaultdict
# d = defaultdict(list)
# words = sentence.split()
# for word in words:
#    d[word[0]].append(word)
#
# print(d)










# my_string = 'hellohai'
# #
# new_string = ''.join(['-' if my_string.count(i) > 1 else i for i in my_string])
# print(new_string)


# class Login:
#     login_count = 0  # Class Variable that keeps count of login counts
#
#     def __init__(self):
#         Login.login_count += 1
#
# u1 = Login()
# print(Login.login_count)









# class Simple:
#     def __init__(self, items):
#         self._items = items
#
#     def __iter__(self):
#         return iter(self._items)
#
# s = Simple([1, 2, 3, 4, 5])
#
# for item in s:
#     print(item)

'''
22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a
'''


# class MyDict:
#     def __init__(self, d):
#         self._dict = d
#
#     def __getitem__(self, item):
#         return self._dict[item]
#
#     # __getattr__ method is called only for missing attributes.(i.e. if you try to access an attribute
#     # which is not in instance dict)
#     def __getattr__(self, name):
#         return self._dict[name]
#
# d = MyDict({'a': 1, 'b': 2})
# # d.a
# # 1
# # d.b
# # 2
# # d['a']
# # 1
# # d['b']
#
# print(d.a)
# print(d['b'])















# sentence = "Hello world. Welcome to Python"
# words = sentence.split()
#
# d = {word: len(word) for word in words}
# print(max(d.items(), key= lambda item: item[-1]))


# a = ("a", "b", 'c', 'f')
# b = ''.join(a)
# print(b)
# b = '.'.join(a)
# print(b)
# a = ['a', 'b', 'c', 'd']
# print(''.join(a))
#
# a = ('a', 'b', 'c', 'd')
# print(''.join(a))

# a = {'a', 'b', 'c', 'd'}
# print(''.join(a))

'''lines = """CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical"""
'''


# from collections import defaultdict
# _errors = defaultdict(int)
# for line in lines.split('\n'):
#
#     # a, b = line.strip().split(':')
#     # _errors[a] += 1
#     # print(line)
#     # Split the line based on newline character
#     #     Split each line based on ":" to separate out error message part.
#
#     error_type, other = line.strip().split(':')
#     _errors[error_type] +=1
#
# print(_errors)




# a = ['abc', '123', 'hello', '23']
# for item in a:
#     if item.isdigit():
#         print(item)



# a = [1, 2, 3, 4, 5]
# squares = lambda number: number ** 2
# # print(list(map(squares, a)))
# b = [ squares(item) for item in a]
# print(b)






# l = [[1,2,3],[4,5,6],[7,8,9]]
# total = sum([sum(item) for item in l])
#
# print(total)






# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# # Replace "nose" with "net"
# for key, value in d.items():
#     if isinstance(value, dict):
#         d[key]['n'] = "net"
# print(d)








# import re
# white_spaces = 0
# with open(path) as f:
#     for line in f:
#         match = re.findall(r'\s', line)
#         if match:
#             white_spaces += len(match)
# print(white_spaces)










#54 Grouping anagrams.

# from collections import defaultdict
# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# d = defaultdict(list)
# for word in words:
#     print(word)
#     s = ''.join(sorted(word))
#     print(s)
#     d[s].append(word)
#     print(d)

# print(d)





# point =  {'a': 1, 'b': 2}
# print(point.get('c', 'Sorry the key does not exist'))



# evens = [ item for item in range(1, 51) if item % 2 == 0]
# even = [ item for item in range(0, 51, 2)]
#
# print(evens)
# print(even)



# names = ['apple', 'google', 'apple', 'yahoo', 'google']

# from collections import defaultdict
# d = defaultdict(int)
# def duplicate(n):
#     for item in n:
#         d[item] += 1
#
#     for key, value in d.items():
#         if value > 1:
#             print(key)
#
# duplicate(names)


# unique_items = set(names)
#
# for item in unique_items:
#     _count = 0
#     for name in names:
#         if item == name:
#             _count += 1
#     if _count > 1:
#         print(item)









# def is_prime(number):
# # 'any' ---> is a builtin function that returns True if any one item in iterable evaluates to  boolean True
# 	return not any([number % i == 0 for i in range(2, number)])
#
#
# print(is_prime(5))


# a = 1234
# s = a % 10
# print(s)











# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
# ]
#
# from collections import Counter
# c = Counter(words)
#
# print(c)
# print(c.most_common(2))










# from math import sqrt
# def is_perfect_square(number):
#     return number == sqrt(number) ** 2
#
# print(is_perfect_square(5656898989))





# def square(number):
#     for i in range(1, number):
#         if number == i * i:
#             print("true")
#     else:
#         print("Fail")
#
# square(5656898989)



# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
#
# d = {name:names.count(name) for name in names if names.count(name) > 1}
# print(d)
# print(len(names))













# from collections import defaultdict
#
# with open(path) as f:
#     # declare a default dictionary
#     d = defaultdict(int)
#     # Iterate over each line in the file object
#     for line in f:
#         # Check if the line has atleast one character
#         if line.strip():
#             # Split the line on white space
#             words = line.split()
#             # Iterate through each word in words list and build a dictionary with word and count pair
#             for word in words:
#                 d[word] += 1
#
#     print(d)






# for i in range(1, 6):
#     print(f"{'*'*i:<5}")

# for i in range(1, 6):
#     for j in range(1, 11):
#
#         if i == j or i > j :
#             print('*', end = ' ')
#         else:
#             print(' ')








# # Equilateral Triangle
# for i in range(1, 6):
#     print(f"{'* '*i:^10}")













# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# from collections import deque
# def _rotate(iterable, n):
#     d = deque(iterable)
#     print(d)
#     d.rotate(n)
#     return list(d)
#
# print(_rotate(names, 1))





















# sentence = "hello world welcome to python hello hi how are you hello there"
#
# import re
#
# def index_nth_occurance(sentence, pat, n):
#     matches = re.finditer(pat, sentence)
#     # print(list(matches))
#     _count = 0
#     for match in matches:
#         _count +=1
#         if _count == n:
#             return f"Start Index: {match.start()}, End Index: {match.end()}"

# print(index_nth_occurance(sentence, 'hello', 3))

















# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
#
# from collections import defaultdict
# d = defaultdict(list)
#
# for item in items:
#     _item, group = item.split('-')
#     d[group].append(_item)
#     d[group] += (_item)
#
# print(d)







# sentence = "Hi there! How @ar!e you:) How are you doing today!"
# import re
# # words = re.findall(r'\b\w+', sentence.lower())
# words = re.findall(r'\w+', sentence.lower())
# print(words)

# from collections import Counter
# sentence = "i am a boy  and i am dont want to do anything with put their order  so i want to say none "
# words = sentence.split()
# print(words)
# s = Counter(words)
# print(s)












# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# max_numbers = max(numbers)
# all_max = [number for number in numbers if number == max_numbers]
# print(all_max)

#
# from collections import Counter
# sentence = "hello world hi apple you yahoo to you"
# words = sentence.split()
# word = max(words, key = len)
# s = [item for item in words if len(item)==len(word)]
# print(s)











sentence = '0-0, 4-8, 20-20, 43-45'
# Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]

# word = sentence.split(',')
# k = []
# for item in word:
#     # print(item)
#     _for = item.split('-')
#     si, ei = _for
#     for sen in range(int(si), int(ei)+1):
#         k.append(sen)
#
# print(k)






#106


# class Parent:
#     @staticmethod
#     def demo():
#         print('Running demo in Parent')
#
# class Child(Parent):
#     @staticmethod
#     def d():
#         print('Running demo in Child')
#         super().demo()
#
# c = Child()
# c.d()






#107 Write a function which returns the sum of lengths of all the iterables


# def total_length(*iterables):
#     total = 0
#     for i in iterables:
#         total += len(i)
#     print(total)
#
#
# total_length([1, 2, 3], (4, 5))











# # 109 Replace all vowels with "*"
# import re
# sentence = "hello world welcome to python"
# words = re.sub(r'[aeiou]', '*', sentence)
# print(words)
# # h*ll* w*rld w*lc*m* t* pyth*n




# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# l = []
# for i in l1:
#     for j in l2:
#         l.append(str(i)+j)
#
# print(l)













# word = "AAAAaaccYYY"
# unique_letters = set(word)
# print(unique_letters)
#
# count = [ ''.join((letter, str(word.count(letter)))) for letter in unique_letters ]
# print(count)





# a = [3, 5, -4, 8, 11, 1, -1, 6]
#
# for item1 in a:
#     for item2 in a:
#         if item1 != item2:
#             if item1 + item2 == 10 or item1 - item2 == 10:
#                 print((item1, item2))









# numbers = [1234567890, 123456790, 1234567890]
#
# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         # numbers, = args
#         prefix_numbers = [ "+91-"+str(number) for number in numbers ]
#         return func(prefix_numbers)
#     return wrapper
# @prefix_country_code
# def print_numbers(numbers):
#     for number in numbers:
#         print(number)
#
# print_numbers(numbers)






# a = ['992', '334', '252']
# # result = []
# #
# for i in range(len(a)):
#     if i == 0:
#         b = sorted(a[i])
#         print(b)
#     elif i == 1:
#         c = sorted(a[i])
#         print(c)
#     elif i == 2:
#         d = sorted(a[i])
#         print(d)
# for item in [b, c, d]:
#     min, *mid, max = item
#     result .append(int(min) + int(max))
#     # output = sorted(result)
# output = sorted(result)
# print(output)



# a = [998, 556, 456]
# k = []
# for item in a :
#     if isinstance(item, int):
#         l = str(item)
#     min, *mid, max = l
#     k.append(int(min)+int(max))
#
# output = sorted(k)
# print(output)


# ab = {(10, 20): 10, (20, 30): 40, (30, 40): 30}
# s = []
# k = ab.keys()
# for item in ab.keys():
#     s.append(item[0])
# sort_= sorted(s)
# secmax = sort_[-2]
# d = []
# for char in ab.keys():
#     d.append(char)
# for val in d:
#         # print(val)
#     if secmax == val[0] :
#         print(ab[val])






