# Dunder essentially means double under

class Person:

    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age

    def __del__(self): # desctructor
        print("Object is being deleted") 

p = Person("mike", 25)

class Vector:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __add__(self, other): # magic function
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self): # if the variable represents a vector then it will return the following
        return f"X: {self.x}", "Y: {self.y}" 

    def __len__(self): 
        return 10

    def __call__(self): # when you call an object
        print("You called me?")


v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2

print(v3.x)
print(v3.y)