# decorators wrap a function with additional functionality

def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating the function")
        return function(* args, ** kwargs)
    
    return wrapper

@mydecorator # this is decorating the "string" function with the function of "mydecorator"
def string(person):
    return f"Hello {person}"

string("Mike")

