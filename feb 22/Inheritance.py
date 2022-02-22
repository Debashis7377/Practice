# class parent:
#     def __init__(self, value):
#         self.value = value
#
#     def google(self):
#         print(f"Executing parent google {self.value}")
#
#     def apple(self):
#         print("Executing parent Apple")
#         self.google()

# p = parent(10)
# print(p.value)
# p.google()
# p.apple()

#     child class having a separate method
# class child1(parent):
#     def demo(self):
#         print("Executing Demo")



# c = child1(10)
# c.google()
# c.apple()
# c.demo()


'''                '''

# class parent:
#     def __init__(self, value):
#         self.value = value
#
#     def google(self):
#         print(f"Executing parent google {self.value}")
#
#     def apple(self):
#         print("Executing parent Apple")
#         self.google()
#
# class child1(parent):
#     def demo(self):
#         print("Executing Demo")
#
# # child overriding parent class method
# class child2(parent):
#     def hello_world(self):
#         print("hello world")
#
#     def google(self):                                             # child overriding parent class, cause we modify it
#         print(f"Executing child2 Google {self.value}")
#
#
#
# # c = child2(20)
# # c.hello_world()
# # c.google()
# # c.single()                  # Attribute Error         cause single attribute is not present in parent nd child class
# # print(child2.__mro__)                    #(<class '__main__.child2'>, <class '__main__.parent'>, <class 'object'>)
#
#
#
# # child adding extra functionality and reusing the original functionality of the parent class
# class child3(parent):
#     def google(self):
#         print("Executing child3 Google !!!")
#         super().google()                      # super = To access the parent class attribute and class variable but we are not able to access instance variable
#         print("Executing child3 again ", self.value)                              # it may be a class variable , nd an attribute or method
#                                                                                   #  any thing  which is called by dot(.) operator --- > attribute
#
# # c = child3(30)
# # c.google()
#
# # child class is having an extra attribute
#
# class child4(parent):
#     def __init__(self, value, name):
#         self.name = name
#         super().__init__(value)                   # calling parent class constructor
#
# # c = child4(50, "debashis")
# # print(c.name)
# # print(c.value)
# # print(c.__dict__)
#
#
# class facebook:
#     def spam(self):
#         print("Executing Facebook Spam")
#
#
# # child inheriting from multiple parents
#
# class child5(parent, facebook):
#     pass
#
# # c = child5(60)
# # c.google()
# # c.spam()
# # c.apple()
#
# '''   MULTI LEVEL INHERITANCE      '''
#
# class A:
#     def demo(self):
#         print("class A demo")
#
# class B(A):
#     def demo(self):
#         print("class B demo")
#         super(). demo()
#
# class C(B):
#     def demo(self):
#         print("class C demo")
#         super().demo()

# c = C()
# print(c)                                                #<__main__.C object at 0x000001EAA8D73C40>
# print(C.__mro__)                                        #(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)





# class parent:
#     def demo(self):
#         print("class parent demo")
#
# class Demo(parent):
#     def demo(self):
#         print("class child1, demo")
#         super().demo()
#
# class spam(parent):
#     def demo(self):
#         print("class child2, demo")
#         super().demo()
#
# # MULTIPLE INHERITANCE
# class child(spam, Demo):
#     pass


# c = child()
# c.demo()
# print(child.__mro__)
#(<class '__main__.child'>, <class '__main__.spam'>, <class '__main__.Demo'>, <class '__main__.parent'>, <class 'object'>)

'''callable()   # if we want to check a function/ method is callable or not '''
# print(callable(len))




'''
2 types of dictionary is there 
1. class dictionary 
2. Instance dictionary'''

#############################################################
class BankAccount:
    interest_rate = 0.04
    def __init__(self, name , balance):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        if amount < 0 :
            raise ValueError("amount should be greater then 0")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            raise ValueError("insufficient funds")

    def roi(self):
        interest_amount = self.balance * self.__class__.interest_rate
        self.balance += interest_amount


class SBAccount(BankAccount):
    interest_rate = 0.05
    def withdraw(self, amount):
        if amount > 10000:
            raise ValueError("can not withdraw more then 10k ")
        super().withdraw(amount)

class SalaryAccount(BankAccount):
    def __init__(self, name):
        self.is_first_month_salary = True
        self.max_draft_amount = 1000
        self.draft_amount_taken = 0.00
        super().__init__(name, 0.00)

    def deposit(self, amount):
        if self.is_first_month_salary:

            self.is_first_month_salary = False
            super().deposite(amount + 1000)
        else:
            super().deposite(amount)

    def overdraft(self, amount):
        if amount <= self.max_draft_amount:
            self.balance += amount
            self.max_draft_amount -= amount
        else:
            raise ValueError(f"max available draft amount is {self.max_draft_amount}")



class SeniorCitizenAccount(BankAccount):
    interest_rate = 0.06
    def withdraw(self, amount):
        if amount > 20000:
            raise ValueError(" can not withdraw more thrn 20k")

        super().withdraw(amount)

class SukanyaSamrudhiAccount(BankAccount):
    def __init__(self, name, balance):
        if balance < 1000:
            raise ValueError
        super().__init__(name, balance)
    def deposite(self, amount):
        if amount < 1000 :
            raise ValueError("min amount to deposite is 1k")
        super().deposite(amount)

    def withdraw(self, amount):
        raise Exception("You cannot withdraw amount from SSA")




# v = SukanyaSamrudhiAccount("steve", 1000)
# v.deposite(1900)
# v.withdraw(1000)


# sd = SeniorCitizenAccount("debashis", 25000)




# s1 = SalaryAccount("debashis")
# s2 = SalaryAccount("behera")




s = SalaryAccount("Debashis")
s.deposite(50000)


# s = SBAccount("Debashis", 20000)
# print(s.balance)

# s.withdraw(11000)
# s.withdraw(500)

# class Demo:
#     a = 10                       # class variable
#     def demo(self):
#         print("demo", self.__class__.a)
#
# class child(Demo):
#     a = 100                           # Redefining class variable
#     # def demo(self):
#     #     print("child Demo")
#
#
# c = child()
# print(c.__class__)
# c.demo()

class PenaltyAccount:
    def withdraw(self, amount):
        self.balance -= 200
        super().withdraw(amount)
class PensionAccount(PenaltyAccount, BankAccount):
    penalty_amount = 200

class maxTransactionlimit(PensionAccount, BankAccount):
    penalty_amount =  1000

# p = PensionAccount("steve", 10000)
# p.withdraw(1000)

q = maxTransactionlimit("steve", 10000)

q.withdraw(1000)




# class PensionAccount(BankAccount):
#     def withdraw(self, amount):
#         self.balance -= 200               #penalty amount
#         super().withdraw(amount)



# k = PensionAccount("steve", 10000)
# print(k.balance)
# k.withdraw(1000)
# k.balance








