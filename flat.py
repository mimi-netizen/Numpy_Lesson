import numpy as np
ar = np.array([
    [1,2,3],
    [6,5,8]
])

flat_obj = ar.flat 
for i in flat_obj: # type: ignore
   print(i)