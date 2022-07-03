# Zadanie 5. Write a Python Program for Linear Search.
#  Given an array arr[] of n elements, write a function to search a given element x in
#  arr[].

def linearSearch(arr, element) : 
    arr2 = []
    flag = False
    for i in range(len(arr)):
        if element == arr[i] :
            flag = True
            arr2.append(i)
            
    if flag == True:
        print("Element found at index: ")
        for i in arr2:
            print(i)
    

arr = [11, 23, 44, 56, 123, 543, 3211, 87, 0]
print(arr)
element = int(input("Please eneter number from list to check position: "))
linearSearch(arr, element)

