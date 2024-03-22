import numpy as np
ar = np.array(
    [
        [1,2,3],
        [2,1,4]
    ] # (2,3) 2D
)
for i in np.nditer(ar, order="C"):
    print(i)