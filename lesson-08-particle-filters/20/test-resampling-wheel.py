import random
from resamplingwheel import resampling

N = 10
w = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

p3 = resampling(p, w, N)

print(p3)

N = 3
w = [1, 1, 1]
p = [0, 1, 2]

p3 = resampling(p, w, N)

print(p3)
