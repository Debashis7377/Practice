class parent:
    def __init__(self, value):
        self.value = value

    def google(self):
        print(f"Executing parent google {self.value}")

    def apple(self):
        print("Executing parent Apple")
        self.google()

# p = parent(10)
# print(p.value)
# p.google()
# p.apple()

class child1():

