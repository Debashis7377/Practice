'''most importanat notes  '''
# def add(a, b):              # def add(int a, float b):
#     return a+b
#
# def add(a, b, c):           # or      def add(int a, int b, float c) :
#     return a+b+c
# def add(a, b, c, d):
#     return a+b+c+d

# print(add(1,2))      # error
# add = 10
# print(add(1,2,3))         # error

# class demo:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
# d = demo(1,2)              #TypeError: add() missing 1 required positional argument: 'd'


''' we can not have explicit return statement in __init__ .. by default constructor will return NONE '''
'''__init__ is type of a variable name, we can assign value also
__init__ = 10
__init__ = [1, 2, 3, 4] '''

# class point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d

# p1 = point(1, 2)
# p2 = point(1, 2, 3)
# p3 = point(1, 2, 3, 4)     # error


''' we can follow this type of method overloading 
most important notes , interview question 
in this method we have to use default value for method overloaded '''


class point:

    def __init__(self, a=0, b=0, c=0, d=0):        # using defalut value
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def display(self):
        print(self.a + self.b+self.c+self.d)

#
# p0 = point()
# p1 = point(1, 2)
# p2 = point(1, 2, 3)
p3 = point(1, 2, 3, 4)
p3.display()
#
# print(p0.__dict__)
# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)

'''  in java method overloading constructor

class point:
    def __init__(this, a, b):
        this.point(a, b, 0, 0)        # in java this is happen internally so method overloading is acceptable in java 
    def __init__(this, a, b, c):
        this.a = a
        this.b = b
        this.c = c
    def __init__(this, a, b, c, d):
        this.a = a
        this.b = b
        this.c = c
        this.d = d   '''

# #not mandatory
# class demo:
#     def __init__(self, *args):
#         self.args = args
#
# d = demo()
# d1 = demo(1, 2, 3)
# d5= demo(1,2,3,4)
#
# print(d.__dict__)
# print(d1.__dict__)
# print(d5.__dict__)




# def add(a, b):
#     return a+b
#
# add(1, 2)
# print(dir(add))
''' ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', 
'__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__',
 '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__',
  '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
  '__str__', '__subclasshook__']  '''

# any object which has __call__ method that is a callable object

# class greeting:
#     def __init__(self, name):
#         self.name = name
#     def __call__(self):
#         return f"hello.{self.name}"



# g = greeting("debashis")
# print(g())                 # TypeError: 'greeting' object is not callable

# print(g())             # hello.debashis



# class greeting:
#     def __call__(self, name):
#         return f"hello {name}"
#
# g = greeting()
# print(g("debashis"))             # hello debashis



# class sqaures:
#     def __call__(self, numbers):
#         return [number **2 for number in  numbers]
#
#
# s= sqaures()
# print(s([1,2,3,4,5]))                 #[1, 4, 9, 16, 25]

# class sqaure:
#     def __init__(self, numbers):
#         self.numbers = numbers
#     def __call__(self):
#         return [number **2 for number in  self.numbers]


# s = sqaure([1, 2, 3, 4])
# print(s())                  #[1, 4, 9, 16]



# class evens:
#     def __call__(self, numbers):
#         if numbers % 2 == 0:
#             return True
#         else:
#             return False


# function decorator
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log
# def add(a, b):
#     return a + b
#
# @log
# def sub(a, b):
#     return a - b


# class decorator
# class log:
#     def __init__(self, func):
#         self.func = func
#
#     # very similar to wrapper function
#     def __call__(self, *args, **kwargs):
#         print(f"__call__ calling {self.func.__name__}")
#         return self.func(*args, **kwargs)
#
#
# @log
# def add(a, b):           # add is a object instance of class log
#     return a + b
# # sub = log(sub)         sub pointing to wrapper function . because log returns referance of wrapper function
# @log
# def sub(a, b):               ## sub is a object instance of class log
#     return a - b
#
#
# # add(1, 2)                   # __call__ calling add
# # sub(5, 6)                      #__call__ calling sub
#
# print(add(1, 2))               #__call__ calling add
#                                 #3
# print(sub(5, 6))              #__call__ calling sub
#                               #  -1

# class record:
#     def __init__(self, func):
#         self.func = func
#         self._count = 0
#
#     # very similar to wrapper function
#     def __call__(self, *args, **kwargs):
#         self. _count += 1
#         return self.func(*args, **kwargs)
#
#
# @record
# def add(a, b):
#     return a+b
#
# @record
# def sub(a, b):
#     return a-b
#
# print(add(1, 2))
# print(add(2, 3))
# print(sub(6, 5))
#
# print(add.__dict__)         # {'func': <function add at 0x000001AB5CEBA8C0>, '_count': 2}
# print(sub.__dict__)         # {'func': <function sub at 0x000001AB5D308700>, '_count': 1}



# items = ["deb", "ashis", "janiji", "asasa"]

# by_last = sorted(items, key = lambda item:item[-1])
# print(by_last)

# or

# def last_chr(item):
#     return item[-1]
# by_last = sorted(items, key = last_chr)
# print(by_last)

# # lambda expression (callable)
# lambda_get_last_chr = lambda item: item[-1]


# class get_last_char:
#     def __call__(self, item):
#         return item[-1]
'''
1.     key arguments takess a callable .
2.     functions are callable
3.     lambda functions are callable 
4.     class which have implemented  __call__ methods are also callable'''

# by_last = sorted(items, key = get_last_char() # or g)
# by_last = sorted(items, key = last_chr)
# by_last = sorted(items, key = lambda_get_last_chr)








