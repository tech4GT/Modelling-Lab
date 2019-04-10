""" Simulates a random walk """
import random


def dirn(pos):
    direction = None
    if pos > 0:
        direction = "up"
    else:
        direction = "down"
    return direction


T = int(input("Number of Samples?\n"))
n = int(input("Number of steps you want to simulate?\n"))
p = float(input("Odds of Going up?\n"))*100

vals = []

for t in range(0, T):

    pos = 0

    for i in range(n):
        if random.randint(1, 100) <= p:
            pos += 1
        else:
            pos -= 1

    vals.append(pos)

    direction = dirn(pos)
    pos = abs(pos)
    print("Final position is " + str(pos) + " " + direction)

avg = 0
for el in vals:
    avg += el
avg /= T
avg = round(avg)

var = 0
for el in vals:
    var += ((el-avg)*(el-avg))
var /= n
var = round(var)

print("\nThe mean of the outputs is: " + str(avg) + " " + dirn(avg))
print("The variance of the output is " + str(var))
