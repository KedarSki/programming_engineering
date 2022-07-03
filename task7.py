## Zadanie 7. 


import re
def eatvowels(string):
    return (re.sub("[aeiouAEIOU]","",string))

string = input("Please input the work you would like to eatvowels from: ")
print(eatvowels(string))