#Write code that outputs p after multiplying each entry
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
def normalize(probalities):
    s = sum(probalities)
    for count in range(len(probalities)):
        probalities[count] = probalities[count] / s

    return probalities

check=[0, 1, 1, 0, 0]
for count in range(len(p)):
    if check[count]:
        p[count] = p[count] * pHit
    else:
        p[count] = p[count] * pMiss

p = normalize(p)

print(p)
