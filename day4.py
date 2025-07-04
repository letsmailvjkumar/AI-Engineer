# list comprehensions
import re
# lst = [2, 3, 4, 5, 6, 7]
# res = [val ** 2 for val in lst[::2]]
# print(res)
#
# a = [1, 2, 3, 4, 5]
# res = [val for val in a if val % 2 == 0]
# print(res)
#
# b = [i for i in range(0,10)]
# print(b)
#
# coordinates = [(x,y) for x in range(3) for y in range(3)]
# print(coordinates)

# Nested List Comprehension with Slicing
# c = [[1,2], [3,4], [5,6]]
# d = [y for row in c[:2] for y in row]  # range to 2 sublist(i.e (1,2), (3,4)), then list comprehension
# print(d)
#
# def cleanText():
#     with open('messyText.txt', encoding='utf-8') as f:
#         res = [
#             re.sub(r'<.*?>', '',  # remove HTML tags
#                    re.sub(r'[^a-zA-Z0-9\s]', '',  # remove special characters
#                           line.strip().lower()))  # strip whitespace and lowercase
#             for line in f.read().splitlines()
#         ]
#         print(res)
# cleanText()

def wordFrequency():
    word = str(input("Enter a word: "))
    print(len(word))

wordFrequency()