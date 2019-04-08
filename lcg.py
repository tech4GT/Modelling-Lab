x = int(input("Please enter the seed value\n"))
a = int(input("Please enter the value of a\n"))
c = int(input("Please enter the value of c\n"))
m = int(input("Please enter the value of m\n"))


if(m < 0):
    print("Modulus negative")
    exit(0)
if(a <= 0 or a >= m):
    print("a out of bounds")
    exit(0)
if(c < 0 or c >= m):
    print("c out of bounds")
    exit(0)
if(x < 0 or x >= m):
    print("Seed out of bounds")
    exit(0)

n = int(input("Please enter the count of number you want to generate\n"))

for i in range(n):
    x = (a*x + c) % m
    print(x)
