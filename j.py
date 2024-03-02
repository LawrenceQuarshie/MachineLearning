import numpy as np

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = np.percentile(nums, 75) # calculates the 75 percentile of the given dataset

print(x)