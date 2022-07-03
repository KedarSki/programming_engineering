## Zadanie 4. Sprawdzanie duplikatów. 
from collections import Counter
from multiprocessing.reduction import duplicate


string = input("Enter text to check duplicates: ")
duplicates = []

for i in string:
        if string.count(i) > 1:
            if i not in duplicates:
             duplicates.append(i)
print("Following letters has been duplicated", duplicates)