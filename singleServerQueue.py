import random


class Job:
    def __init__(self, at, st):
        self.at = at
        self.st = st
        self.wt = None
        self.et = None

    def arrive(self, q, et):
        self.et = et
        q.append(self)

    def depart(self, t):
        self.wt = t-self.at


Q = []

t = int(input("Time for which you want to simulate\n"))
n = int(input("Number of Jobs in the system\n"))
x = int(input("Enter the max waiting time\n"))
jobs = []

for i in range(n):
    jobs.append(Job(random.randint(0, t), random.randint(0, x)))

t = 0

count = 0
while(count < n):
    for j in jobs:
        if t == j.at:
            j.arrive(Q, t)
    if not not Q and Q[0].et + Q[0].st <= t:
        Q.pop(0).depart(t)
        count += 1
    t += 1


avg_wt_time = 0
for el in jobs:
    avg_wt_time += el.wt
avg_wt_time = avg_wt_time/n

print("Average wait time is " + str(avg_wt_time))
