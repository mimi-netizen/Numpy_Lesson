import numpy as np
ar = np.array([
    [1,2,3],
    [5,6,7]
])
for i, v in np.ndenumerate(ar):
    print(i,v)