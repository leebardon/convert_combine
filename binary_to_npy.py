import pandas as pd
import numpy as np
import os 
import sys 

month = sys.argv[1]
root = os.environ["root"]
binary = os.environ["binary"]
out_filename = "month{}.npy".format(month)

data = np.fromfile(f'{binary}', dtype='>f4', count=-1)
data = data.byteswap().newbyteorder()
arr = data.reshape((144,90,22))
sliced = arr[:,:,0]

np.save(f'{root}/{out_filename}', sliced)


