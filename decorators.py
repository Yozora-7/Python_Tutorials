# decorators wrap a function with additional functionality

def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating the function")
        return function(*args, ** kwargs)
    
    return wrapper

@mydecorator # this is decorating the "string" function with the function of "mydecorator"
def string(person):
    return f"Hello {person}"

string("Mike")

# Logging example

def logs(function):
    def wrapper(**args, **kwargs):
        value = function(**args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

@logs
def add(x, y):
    return x + y

print(add(10, 20)) # without the decorator, the function above would just print 30, as that is x + y. When the decorator is called, it will then print the string.

# Timing example

import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute")
        return value
    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result

myfunction(10000)
