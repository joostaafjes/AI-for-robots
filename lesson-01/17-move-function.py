#Program a function that returns a new distribution
#q, shifted to the right by U units. If U=0, q should
#be the same as p.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = p
    if U > 0:
        for i in range(U):
           q.insert(0, q.pop())
    elif U < 0:
        for i in range(-U):
           q.append(q.pop(0))
    return q

print(move(p, -2))
