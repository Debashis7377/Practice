'''names = ['apple', 'mango', 'tango']



print('apple' in names)      #
print(names[0]) #names.__getitem__(0)
len(names)        # names.__len__()
names[0] = 'instagram'      # names.__setitem__(0, 'instagram')
names.__delitem__(0)      # it will delete the 0th position value 

a = 10
# len(a) '''           # internally --------- a.__len__()        # error

# class point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# p = point(10, 20)
# print(p)               # <__main__.point object at 0x000002D1748D9A50>
# print(len(p))             #  TypeError: object of type 'point' has no len()
# we dont have magic method in this class point , so all these are throwing errors












class point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __len__(self):
        print("__len__")
        return 2

    def __contains__(self, item):
        print(f"checking if {item} in point objects")
        return item in self.__dict__.values()          # list.__contains__(item)


    def __getitem__(self, index):
        if index == 0 :
            return self.a
        elif index == 1:
            return self.b
        else:
            raise IndexError('index out of range')


    def __setitem__(self, index, value):
        if index == 0:
            self.a = value
        elif index==1 :
            self.b = value
        else:
            raise IndexError

    def __delitem__(self, value):
        print("__delitem__")
        raise Exception()


# p = point(1, 2)
# p2 = point(1.5, 2.5)
# print(len(p))           # 2
# print(len(p2))          # 2
# print(p.__len__())      # 2

# print(1 in p)
# print(20 in p)


# print(p[0])           # __getitems__
# print(p2[1])


