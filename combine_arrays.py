import numpy as np
import os

npypath = f'{os.getcwd()}/depth0/'

print("\n")
print("Month 1 forms the base...", "\n")

def stack(filepath, i):
    combined = np.load(f'{npypath}combined.npy')
    loaded = np.load(f'{filepath}')
    stacked = np.dstack((combined, loaded))
    np.save(f'{npypath}combined.npy', stacked)
    print("-----> Month", i, "added to array <-----")
    print("Shape: ", stacked.shape)

for i in range(2, 4):
    filepath = f'{npypath}month{i}.npy'
    stack(filepath, i)



