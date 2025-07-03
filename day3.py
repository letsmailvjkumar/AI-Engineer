# - Functions, lambda, comprehensions
# - Case Study: Clean a messy text dataset using list comprehensions
# - Mini-project: Word frequency analyzer for a user-provided paragraph

def evenOdd(x: int) ->str:  # type_hints -> Tell explicitly the data type and return type
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(evenOdd(2))

#Types of function arguments: 4 Types -> Default, Keyword, Positional, Arbitrary keyword(*args, **kwargs)

def myFun(x, y=10):         # default argument
    print(x)
    print(y)

myFun(3)

def student(fname, lname):   # keyword argument -> pass parameter name and value, no need to remember the order
    print(fname, lname)

student(fname='Aki', lname='Kumar')
student(lname="david", fname='goggins')

def nameAge(name: str, age: int) ->str:            # Positional arguments -> use the positional argument if we know the order of arguments
    return f"My name is {name} and I am {age} years old"

print(nameAge('John', 20))  # case 1: My name is John and I am 20 years old
print(nameAge(20, 'Alice')) # case 2: My name is 20 and I am Alice years old

def myFun(*args):                        # *args -> use variable number of positional arguments (tuple)
    return sum(args)

print(myFun(1,2,3,4))

def keyValue(**kwargs):                 # **kwargs -> use variable number of keyword arguments (dict)
    for k, value in kwargs.items():
        print("%s : %d" % (k, value))

keyValue(a=1,b=2,c=3)

def outer():                            # Nested functions
    s = "I'm outside Function"
    def inner():
        print(f"I'm inside function calling, {s}")

    inner()

outer()

cube = lambda x: x ** 3  # Anonymous function -> use 'lambda' as keyword
print(cube(7))

def factorial(n):        # Recursion Function
    if n==0:
        return 0
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def myFun1(x):             # pass-by-object reference
    x[0] = 20

lst = [10, 11, 12, 13, 14, 15]
myFun1(lst)
print(lst)


def myFun2(x):
    x=[10,20, 40]

lst = [10, 11, 12, 13, 14, 15]
myFun2(lst)
print(lst)

def swap(x, y):
    temp = x
    x = y
    y = temp

x = 2
y = 3
swap(x, y)
print(x)
print(y)