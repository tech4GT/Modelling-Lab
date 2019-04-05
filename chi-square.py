from scipy.stats import chisquare
from scipy import stats
import numpy as np


print(chisquare([16, 18, 16, 14, 12, 12]))
print(chisquare([16, 18, 16, 14, 12, 12], f_exp=[16, 16, 16, 16, 16, 8]))

x = np.linspace(-15, 15, 9)
print(stats.kstest(x, 'norm'))
