class consologer:
    def log(self, message):
        print(message)

class Textlogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message)
        self.file.write("\n")
        self.file.flush()
#
#
# f = open("text.txt", 'w')
# t = Textlogger(f)
#
import csv

class CSVLogger:
    def __int__(self, file):
        self.file = file

    def log(self, message):
        writer = csv.writer(self.file)
        words = message.split()
        writer.writerow(words)
        self.file.flush()
#







class FilteredConsoleLogger(consologer):
    def __init__(self, pattern):
        self.pattern = pattern

    def log(self, message):
        if self.pattern in message :
            super().log(message)

class FilteredTextLoger(Textlogger):
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)       # initializing parent class

    def log(self, message):
        if self.pattern in message:         #  extra functionality added to child class
            super().log(message)            # original functionality from parent claass


class FilteredCSVLogger(CSVLogger):
    def __int__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)        # initializing parent class cont.

    def log(self, message):
        if self.pattern in message:           # extra funcrtionality added to child class
            super().log(message)             # original function from parent class


class FilteredLogger:
    def __init__(self, pattern):
        self.pattern = pattern

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# mixin class
class FilteredConsoleLogger(FilteredLogger, consologer):
    def __init__(self, pattern):
        FilteredLogger.__init__(self, pattern)
class FilteredTextLogger(FilteredLogger, Textlogger):
    def __init__(self, pattern, file):
        FilteredLogger.__init__(self, pattern)
        Textlogger.__init__(self, file)
class FilteredCSVLogger(FilteredLogger, CSVLogger):
    def __init__(self, pattern, file):
        FilteredLogger.__init__(self, pattern)
        CSVLogger.__init__(self, file)

fcl = FilteredConsoleLogger("error")

fcl.log("this is an error message")
fcl.log('this is an info message')


# f = FilteredLogger('error')
# f.log('this is an error message')         # AttributeError: 'super' object has no attribute 'log'


# c = consologer()
# fcl = FilteredConsoleLogger("error")
# # fcl.log("this is an error message")
# #
# # fcl.log("this is an info msg")
# # fcl.log("this is an warning msg")
# # fcl.log("something gone wrong......error")
#
#
# f = open('test.txt', 'w')
# ftl = FilteredTextLoger("error", f)


# ftl.log('thia is an error message')
# ftl.log('this is new info msg')
# ftl.log('this is an extra msg')
# ftl.log('this is an error wala info')
# ftl.log("this is a new error")


