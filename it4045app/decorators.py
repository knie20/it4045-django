__author__ = 'Andrew'

def decorator(argument):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print (argument)
            # print args[0]
            # print "inner function"
            func(args)
        return wrapper
    return actual_decorator

@decorator("helo")
def hello(a):
    print ('')

hello("f", "alsdkfn", keyword="value")
# func = decorator(hello, "askdjfn")
# func()

# a = str
#
# print a(34)

