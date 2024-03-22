import numpy as np
lst = [1,2,3,45,67,8,9]
dict = {1:"pink", 2:"gray", 3:"black"}
print(type(lst))
ar = np.fromiter(dict.values(), dtype=np.chararray)
print(ar)
print(type(ar))