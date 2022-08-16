class BankAccount:
    interest_rate = 0.4          # class variable
    #all the customer will share the same value or interest rate
    def __init__(self, name, balance=0):
        # instance variables(each customer will get a fresh copy of name , balance and transaction
        self.name = name                                  # instance variable
        self.balance = balance                            # instance variable
        self.transaction = []                             # instance variable
        self.transaction.append(f"***********initial amount deposited {balance}***********")


    def deposite(self, amount):
        self.balance = self.balance + amount
        self.transaction.append(amount)
        print(f"ammount deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance = self.balance - amount
        self.transaction.append(f"amount withdrawn{amount}")
        return f"please collect the cash{amount}"

    def transfer(self, to_account, amount):
        if self.balance < amount:
            raise ValueError("insufficient funds")
        to_account.deposite(amount)
        self.balance -= amount

    def statement(self):
        for transaction in self.transaction:
            print(transaction)
        print("*" * 20)
        print(f"available balance in the account {self.balance}")

    def roi(self):
        interest_ammount = self.balance * BankAccount.interest_rate
        self.balance += interest_ammount
        self.transaction.append(f"******* interest amount credited ******{interest_ammount}")


c1 = BankAccount("debashis", 1000)    # c1 is the instance of class( BankAccount )
c2 = BankAccount("ashis", 5000)
c3 = BankAccount("deb")


# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)

c1.deposite(1000)
# c2.deposite(5000)
# c3.deposite(10000)
# print(c1.balance)

# c1.withdraw(500)
# # c1.withdraw(2000)
# c2.withdraw(2000)
# c3.withdraw(300)

# print(c1.balance)


# c1.deposite(10000)
#
# c1.trnasfer(c2, 10000)
# print(c2.balance)
# print(c1.balance)


c1.statement()


# c1.roi()
# print(c1.balance)

# Counting number if instances created to the class
'''class Demo:
    count = 0      # class variable 
    # shares across all the instance 
    def __init__(self, a, b):
        self.a = a
        self.b = b
        Demo.count += 1

d1 = Demo(1,2)
print(Demo.count)
d2 = Demo(3, 4)
print(Demo.count)
d3 = Demo(10, 3)
print(Demo.count) '''














# for transaction in c1.transaction:
#     print(transaction)