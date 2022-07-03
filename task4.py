# Zadanie 4 Given a string, write a Python program that finds all the duplicate
# characters which are similar to each others


from collections import Counter
from multiprocessing.reduction import duplicate


string = input("Enter text to check duplicates: ")
duplicates = []

for i in string:
        if string.count(i) > 1:
            if i not in duplicates:
             duplicates.append(i)
print("Following letters has been duplicated", duplicates)