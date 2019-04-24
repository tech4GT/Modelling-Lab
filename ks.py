from scipy import stats
import numpy as np


x = np.array([0.23, 0.06, 0.89, 0.19, 0.05])
print(stats.kstest(x, 'uniform', N=5))
