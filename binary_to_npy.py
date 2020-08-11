import pandas as pd
import numpy as np
import os 
import sys 

month = sys.argv[1]
root = os.environ["root"]
binary = os.environ["binary"]
out_filename = "month{}.npy".format(month)

arr = np.fromfile(f'{binary}', dtype='>f4')
#data = data.byteswap().newbyteorder()
arr.shape = (22,90,144)
sliced = arr[0]

np.save(f'{root}/{out_filename}', sliced)


