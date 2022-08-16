from collections import defaultdict, Counter
from itertools import islice
from collections import deque
path = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\txt_log_files\sample.txt"
path_ = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\txt_log_files\access-log.txt"


''' wap to print line number and line in the file'''

# with open(path) as file:
#     for line_no, line in enumerate(file):
#         print(line_no, line)

''' wap to count the number of words in the given file '''

# with open(path) as file:
#     count = 0
#     for line in file:
#         a = line.split()
#
#         for i in a :
#             count += 1
#     print(count)
#  or
# with open (path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         count +=len(words)
#     print(count)

''' wap to print the lines from the last of the file '''

# with open(path) as file:
#     # print(list(file))
#     for line in reversed(list(file)):
#         print(line)

''' wap to count the number of spaces in the given file'''
# with open(path) as file:
#     count = 0
#     for line in file:
#         for char in line:
#             if char == " ":
#                 count += 1
#     print(count)

# or

# with open(path) as file:
#     count = 0
#     for line in file:
#         spaces = line.count(" ")
#         count += spaces
#     print(count)

''' wap to count the number of words which is starting with vowels'''

# with open(path) as file:
#     count = 0
#     for line in file:
#         spl = line.split()      # for char in line.split()
#         for char in spl:
#             if char[0].lower() in "aeiou":
#                 count += 1
#     print(count)

''' wap to creat a dictionary of word and its count pair in the given file '''
# with open(path) as file:
#     d = {}
#     for line in file:
#         word = line.split()
#         for item in word:
#             if item not in d:
#                 d[item] = 1
#             else:
#                 d[item] += 1
#
#     print(d)

# or

# with open(path) as file:
#     d = defaultdict(int)
#     for line in file:
#         word = line.split()
#         for item in word:
#             d[item] += 1
#     print(d)

''' wap to extract all the ip addresses from access log .txt file'''

# with open(path_) as file:
#     l = []
#     for line in file:
#         if line.strip():               # check for the blank line in the file
#             word = line.split()
#             l.append(word[0])
#     print(l)

''' wap to create a dictionary of ip addresses and their count '''

# with open(path_) as file:
#     d = {}
#     count = 0
#     for line in file:
#         if line.strip():
#             word = line.split()
#             if word[0] not in d:
#                 d[word[0]] = 1
#             else:
#                 d[word[0]] += 1
#     print(d)

# or
# with open(path_) as file:
#     l = []
#     for line in file:
#         if line.strip():               # check for the blank line in the file
#             word = line.split()
#             l.append(word[0])
#     # print(l)
# ip_ = Counter(l)
# print(ip_)
# print(ip_.most_common(5))

# with open(path) as file:
#     n = 3
#     for line_no, line in enumerate(file, start=1):
#         if line_no == n:
#             print(line)
# # or
#
# with open(path) as file:
#     count  = 0
#     for line in file:
#         count +=1
#         if count == n:
#             print()

''' wap to print up to nth line '''
# n = 3
# with open(path) as file:


''' wap to print first nth line '''
# n = 2
# with open(path) as file:
#     res = islice(file,n)
#     print(list(res))

# or
#
# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         if line_no <= n:
#             print(line)

''' wap to print last n line '''
# n = 2
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     # print(count)
#     file.seek(0)
#     res = islice(file, count-n, count)        # islie(file, 5 , 7)
#     print(list(res))

# using deque
# n = 3
# with open(path) as file:
#     lines = deque(file, n)
#     print(lines)

path1 = r"C:\Debashis\pythonProject\pythonProject\Practice\L\file handelling practice.py"
''' wap to copy the content of sample.txt in to different file '''

# with open(path, 'r') as file_read:
#     with open(path1, 'w') as file_write:
# # with open(path, 'r') as file_read, open(path1, 'w') as file_write:
#         for line in file_read:
#             file_write.write(line)


# d = {'name': 'apple', 'id': 152778}
# e = {"name": "appple", 'id': 656789}
# f = {d[(i.items())] : e[(i.items())] for i in range(len(d))}
# print(f)
#



path = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\txt_log_files\sample.txt"
word = "debashis"
with open(path, "r+") as file:
    # for line in file:
    for line_no, line in enumerate(file):
        if line_no == 3:
            print(line)
            index = file.tell()
            file.seek(index)
            file.write("python")


