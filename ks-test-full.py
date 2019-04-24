import math
vals = [0.05, 0.06, 0.19, 0.23, 0.89]
dist = [0.2, 0.4, 0.6, 0.8, 1]

dAl = float(input("Enter the value of D alpha\n"))
dPlus = 0
for i in range(5):
    dPlus = max(dPlus, dist[i]-vals[i])
print("dPlus is " + str(dPlus))

dM = vals[0]
for i in range(1, 5):
    dM = max(dM, vals[i]-dist[i-1])

print("dPlus is " + str(dM))

D = max(dM, dPlus)
print("Statistic D is " + str(D))

if(D > dAl):
    print("The distribution is not uniform")
else:
    print("The distribution is uniform")
