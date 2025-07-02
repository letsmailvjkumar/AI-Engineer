# - Control flow: `if`, `for`, `while`
# - *Case Study*: Write a program to automatically assign grades based on a CSV of student scores
# - *Mini-project*: Build a simple grade-book manager
from __future__ import print_function
import csv

marks = 45
res = "Pass" if marks>=55 else "Fail"  # Ternary operator
print(res)

num = 2
match num:    # switch case use - match
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")

cnt = 0
while cnt<3:
    print("Hello geek")
    cnt = cnt + 1

d = dict({'x':20, 'y':30})
for i in d:
    print("%s %d" % (i, d[i]))


for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()

fruits = ["apple", "banana", "cherry"]  #iterater concept
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break

score = int(input("Enter the marks: "))

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# print(get_grade(score))

with open("test.csv", 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)  # skip header
    print(f"{header[0]} | Grade")

    for row in csvreader:
        name = row[0]
        try:
            grade = get_grade(int(row[1]))
            print(f"{name} | {grade}")
        except ValueError:
            print("Invalid score for {name}")