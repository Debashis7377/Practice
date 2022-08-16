'''
 here everytghing is public , there is no  protected and private values
 '''



# class point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def demo(self):
#         self.name = "debashis"
# p1 = point(1, 2)
# p2 = point(3, 4)
# print(p1.__dict__)
# p1.demo()
# print(p1.__dict__)
# p2.demo()
# print(p2.__dict__)


# class circle:
#     def __init__(self, radious):
#         self.radious = radious
#
#
#
#     def circumference(self):
#         return 2 * 3.14 * self.radious
#
#
# c1 = circle(5)
# c2 = circle(4)
# c3 = circle(3)
# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)
# print(circle.__dict__)  #{'__module__': '__main__', '__init__': <function circle.__init__ at 0x00000198D809A950>, 'circumference': <function circle.circumference at 0x00000198D809A8C0>, '__dict__': <attribute '__dict__' of 'circle' objects>, '__weakref__': <attribute '__weakref__' of 'circle' objects>, '__doc__': None}




# c = circle(2)
# print(c.circumference())                 #12.56


# class circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     # _attributes represents It's for internal use
#     # getter method
#     @property
#     def radius(self):
#         print("getting the value of radius")
#         return self._radius              # private variable
#
#     #setter method
#     @radius.setter
#     def radius(self, value):
#         print(f"setting the radius to {value}")
#         if value <= 0 :
#             raise ValueError(" Radious should be positive value ")
#         if not isinstance(value, (float, int)):
#             raise TypeError("The radius should be a number")
#         self._radius = value
#
#     def circumference(self):
#         return 2 * 3.14 * self._radius
#
# c = circle(3)
# print(c.__dict__)
# c.radius = "hello"                  #TypeError: The radius should be a number
# print(c.circumference())

# c._radius = 10
# print(c.circumference())
# c.radius

# class person:
#     def __init__(self, fname, lname, age):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#     @property
#     def fname(self):
#         print("getting")
#         return self._fname
#
#     @fname.setter
#     def fname(self, value):
#         print("setting")
#         if not isinstance(value, str):
#             raise TypeError
#         if len(value) > 5:
#             raise ValueError("fname should be less then 5 charectre ")
#         self._fname = value
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value < 10 or value > 60:
#             raise ValueError()
#         self._age = value
#
#
# p = person("steve", "jobs", 12)



# class A:
#     def __init__(self):
#         self._value = 0        # private variable
#         self.value = 10          # public
#
#     def demo(self):
#         print(self._value)
#         print(self.value)
#
#     def _spam(self):
#         print(self._value)
#         print(self.value)
#
#     def hello(self):
#         self._spam()
#         print("hello")
#
# a = A()
# a.demo()
# a._spam()
# a.hello()




# class spam:
#     def __init__(self, text):
#         self.text = text
#
#      # internal method
#     def _clean_text(self, text):
#         return text.strip()
#
#     def split_text(self):
#         temp = self._clean_text(self.text)
#         return temp.split()
#
#     def get_len(self):
#         temp = self._clean_text(self.text)
#         return len(temp)
#
#
# s=spam("        debashis behera       ")
# print(s.split_text())
# print(s.get_len())



# class Demo:
#     def __init__(self):
#         self.__value = 10  # Internally it is stored as _Demo__value
#         self._a = 200     # private variable
#
#     def demo(self):
#         print(self.__value)
#
# d = Demo()
# print(d._a)
# # print(d.__value)           # AttributeError: 'Demo' object has no attribute '__value'
# print(d.__dict__)
#
# print(d._Demo__value)
# d._Demo__value = 15
# print(d._Demo__value)


'''   single underscore attributes are called private  attributes 
      Double underscore attributes are called protected attributes           '''

'''mar 30 '''

# # _attribute are for internal use only  or for internal implimantation purpose
class Account:
    _interest = 0.04
    def __init__(self, name , balance):
        self.name = name
        self.balance = balance
    # not suppose to call this method directly
    def _spam(self):             # it does for internal use only
        print("account _span")

    def demo(self):              # public method
        self._spam()
        print("accout demo")
#
#
# a = Account('debashis', 2000)
# print(a.__dict__)
# print(a.name)
# # print(a.balace)
# a.demo()
# print(a._interest)    # we can do this but we are not suppose to do this



class SBAccount(Account) :
    _interest = 0.05
    def _spam(self):
        print('SBAccount _spam')


sb = SBAccount('sandeep', 1000)
# sb.demo()


class Calculator:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def mul(self):
        return self._a * self._b


# c = Calculator(1, 2)
# print(c.mul())
# c = Calculator('5', 2)
# print(c.mul())
# c = Calculator('5', 1.4)
# print(c.mul())              # TypeError: can't multiply sequence by non-int of type 'float'
''' this is happening because setter function is not there ,,, it is allowing bad values into this functions
to restrict this we are using setter method 
'''
# print(c._a)








class spam:
    def __init__(self, text):
        self.text = text

    # internal method
    def _clean_up(self, text):
        return text.strip()

    def split_text(self):
        temp = self._clean_up(self.text)
        return temp.split()


    def get_len(self):
        temp = self._clean_up(self.text)
        return len(temp)


# s = spam("        hello world welcome to python       ")
# print(s.__dict__)            # {'text': '        hello world welcome to python       '}
# print(s.get_len())          # 29
# print(s.split_text())        # ['hello', 'world', 'welcome', 'to', 'python']













class spam:          # internally it is doing ----------> class spam(object):
    pass


s = spam
print(dir(s))        # it will display all the magic methods
''' this thinga re coming from object class------------>  
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
'''







