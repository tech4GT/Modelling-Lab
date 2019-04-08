import math

seed = input("Enter the seed number\n")
l = len(seed)
seed = int(seed)
n = int(input("Enter the count of numbers to generate\n"))

print("The output numbers are: ")

div = round(math.pow(10, l/2))
rem = round(math.pow(10, l))

for i in range(n):
    seed = math.floor(seed*seed/div) % rem
    print(seed)
