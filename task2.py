#  Zadanie 2  Write Python program (function) for cube sum of first n natural numbers.
#  Print the sum of series 13 + 23 + ....+ n3
#  till n -th term

def cubeSum(n):
    sum = 0
    for value in range(1, n+1):
        sum += value**3
    return sum


n = int(input("Enter the value of n : "))

print("Cube sum : ", cubeSum(n))