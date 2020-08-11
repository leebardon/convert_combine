import numpy as np
import os

os.chdir(f'{os.getcwd()}/depth0/')
N = int(os.environ["num_months"])
N+=1

arrays = []
for i in range(1, N):
    arr = np.load(f'month{i}.npy')
    arrays.append(arr)

stacked = np.stack((arrays))
np.save(f'combined.npy', stacked)

