import random

N = 10
w = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

p3 = []
sum_weights = sum(w)
for i in range(N):
    r = random.random() * sum_weights
    sum_till = 0
    for c in range(N):
        sum_till += w[c]
        if sum_till > r:
            break
    print(c)
    p3.append(p[c])

print(p3)
