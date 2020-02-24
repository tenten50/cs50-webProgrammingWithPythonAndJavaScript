name = input()
print(f"hello, {name}!")  #f  fomart string

#python doesn't require you to specify explicitly what the type of the value
i = 28
print(f"hello, {i}")

j = 2.8
print(f"hello, {j}")

m = True
print(f"hello, {m}")

n = None
print(f"hello, {n}")

#how we can import functions from other places in order to use them
from functions import square
print(square(10))

# define a class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 5)
print(p.x)
print(p.y)