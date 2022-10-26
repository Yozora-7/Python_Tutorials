# decorators wrap a function with additional functionality

def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating the function")
        function(* args, ** kwargs)
    
    return wrapper

@mydecorator # this is decorating the "string" function with the function of "mydecorator"
def string(person):
    print("Hello {person}")

string("Mike")

