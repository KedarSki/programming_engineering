# Zadanie 7. Write a comprehension that removes all the vowels (a, e, i, o, u, y) from
# a word written inside a function that you may name eatvowels.
# Example: Test your code on the word ‘Apple Sauce’ ---> ppl Sc


import re
def eatvowels(string):
    return (re.sub("[aeiouAEIOU]","",string))

string = input("Please input the work you would like to eatvowels from: ")
print(eatvowels(string))