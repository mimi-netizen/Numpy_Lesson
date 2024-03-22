import numpy as np
# buffer_obj = b'\x010\x011\x056\x067'
buffer_obj = b'\x01\x04\x05\x07'
ar = np.frombuffer(buffer_obj, dtype=np.uint8)
print(ar)