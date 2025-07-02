# Basics: variables, data types, input/output
# Exercise: Convert a user’s height in feet/inches to centimeters
# Mini-project: Unit converter (temperature, length, weight)

name = input("Enter your name: ")   # I/O Operations
print(name)

x,y = input("Enter two values").split()
print(x,y)

## Output formating - 3 Types
amount = 150.234        #1 using format()
print("Amount: {:.1f}".format(amount))

print("Python", end="@") #2 using sep & end parameter
print("10", "2", "2008", sep="-")

name = "Tushar"         #3 using f-string
print(f"Name: {name}")

num = int(input("Number: "))
add = num + 10
print("The sum is %d" %add)

x = 10
name = "rahul"
print(x)
print(name)

x = "ten"
print(x)

a, b, c = 1, 2.5, "Three" # assigning different values
print(a, b, c)

a=b=c = 100         # assigning the same value
print(a,b,c)

age = input("Enter the age: ")
print(type(age)) # by default input() takes user input as string
s = "10"        # typecasting int(), float(), str()
n = int(s)
print(type(n))

#scope of variable - local, global
def f1():
    z = 10   # local scope
    print(a)

f1()

i = "Iam outside"

def f2():
    # Python analysis the whole function at compile-time and
    # sees an assignment to 'i' below, so it mark 'i' as local.
    # Therefore this print tries to access the local 'i' before it is assigned:
    # print(i)            # error as UnboundLocalError: cannot access variable which is not assigned
    i = "Im inside f2"
    print(i)
f2()

def f3():
    # print(i) Error - 'i' is used prior to global declaration
    global i
    i = "Im inside f3"
    print(i)

f3()

def outer():
    print("outer start")

    def inner():
        print("inner called")

    print("outer before calling inner")
    inner()
    print("outer end")

outer()

x = 5         # create an object for the value 5 and make x reference to it.
y = x         # create y and references the same object as x not x itself.

x = "Geeks"
y = "computer" # here the previous value 5 will be garbage

num = float(input("Number: "))
result = ''

def ft2cm(num):
    res = float(num * 30.48)
    return res

print(format(ft2cm(num),'.2f'))


num = float(input('Enter the number: '))
res = ''

def c2f(num):
    global res
    res = float((num*9/5)+32)
    return res

print(format(c2f(num),'.2f'))

