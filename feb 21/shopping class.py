# class shoppingcart:
#     def __init__(self):
#         self.cart = []
#
#
#     def add_item(self,name, quanity, price ):
#         self.cart.append({"name": name, "quantity": quanity, "price":price})
#
#     def total_cost(self):
#         # total = sum([item["quantity"] * item["price"] for item in self.cart])
#         # return total
#         total = 0.00
#         for item in self.cart:
#             total = total + (item["quantity"] * item["price"])
#         return total
#
#     def remove_item(self, name):
#         for item in self.cart:
#             if item["name"] == name:
#                 if item["quantity"] >1 :
#                     item["quantity"] -= 1
#                 else:
#                     self.cart.remove(item)



# c1 = shoppingcart()
# c2 = shoppingcart()
# c3 = shoppingcart()

# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)
# print(c1)

# c1.add_item("iphone", 1, 800)
# print(c1.cart)
# print(c1.__dict__)

# c1.add_item("imac", 1, 4500)
# print(c1.__dict__)
# c2.add_item("iwatch", 2, 3000)
# print(c2.cart)
# print(c2.__dict__)
# print(c1.__dict__)


# c1.add_item("imac", 1, 4500)
# c1.add_item("iwatch", 2, 3000)
# print(c1.__dict__)
# print(c1.total_cost())

# c1.remove_item("iwatch")
# print(c1.cart)
# c1.remove_item("imac")
# print(c1.cart)


# class shoppingcart:
#     products = {"iphone": 5, "imac": 3, "ipad": 2, "iwatch": 4}
#
#     def __init__(self):
#         self.cart = []
#
#     def add_item(self, name,quantity, price):
#         if name not in self.__class__.products:
#             raise Exception(" Invalid products")
#         elif quantity <= self.__class__.products[name]:
#             self.cart.append({"name": name, "quantity": quantity, "price": price})
#             self.__class__.products[name] -= quantity
#         else:
#             raise ValueError("product out of stock")
#
#
#     def total_cost(self):
#         # total = sum([item["quantity"] * item["price"] for item in self.cart])
#         # return total
#         total = 0.00
#         for item in self.cart:
#             total = total + (item["quantity"] * item["price"])
#         return total
#
#     def remove_item(self, name):
#         for item in self.cart:
#             if item["name"] == name:
#                 if item["quantity"] > 1:
#                     item["quantity"] -= 1
#                 else:
#                     self.cart.remove(item)



# c1 = shoppingcart()
# c2 = shoppingcart()
# c3 = shoppingcart()
# c4 = shoppingcart()
#
# print(shoppingcart.products)
# c1.add_item("iphone", 2, 100)
# c2.add_item("iphone", 2, 800)
# c3.add_item("iphone", 1, 800)
#
#
# print(shoppingcart.products)
#
# c4.add_item("iphone", 1, 800)
# print(shoppingcart.products)


# class shoppingcart:
#     products = {"iphone": 5, "imac": 3, "ipad": 2, "iwatch": 4}
#     prices = {"iphone": 800, "imac":4500, "ipad":4500, "iwatch": 3000}
#
#     def __init__(self):
#         self.cart = []
#
#     def add_item(self, name,quantity, price):
#         if name not in self.__class__.products:
#             raise Exception(" Invalid products")
#         elif quantity <= self.__class__.products[name]:
#             self.cart.append({"name": name, "quantity": quantity, "price": self.__class__.prices[name]})
#             self.__class__.products[name] -= quantity
#         else:
#             raise ValueError("product out of stock")
#
#
#     def total_cost(self):
#         # total = sum([item["quantity"] * item["price"] for item in self.cart])
#         # return total
#         total = 0.00
#         for item in self.cart:
#             total = total + (item["quantity"] * item["price"])
#         return total
#
#     def remove_item(self, name):
#         for item in self.cart:
#             if item["name"] == name:
#                 if item["quantity"] > 1:
#                     item["quantity"] -= 1
#                 else:
#                     self.cart.remove(item)
#
#
#
# c1 = shoppingcart()
# c2 = shoppingcart()
# c3 = shoppingcart()
# c4 = shoppingcart()
#
# # print(shoppingcart.products)
# c1.add_item("iphone", 2, 100)
# print(shoppingcart.products)
# c2.add_item("iphone", 2, 800)
# c3.add_item("iphone", 1, 800)

#
# print(shoppingcart.products)
#
# c4.add_item("iphone", 1, 800)
# print(shoppingcart.products)


















