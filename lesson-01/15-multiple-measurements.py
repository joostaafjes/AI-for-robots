#Modify the code so that it updates the probability twice
#and gives the posterior distribution after both
#measurements are incorporated. Make sure that your code
#allows for any sequence of measurement of any length.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
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

def run_all_measurements(start):
    state = start
    for count in range(len(measurements)):
        state = sense(state, measurements[count])

    return state

final_state = run_all_measurements(p)

print(final_state)
