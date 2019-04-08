from scipy import stats
import numpy as np


print(stats.chisquare([16, 18, 16, 14, 12, 12]))
print(stats.chisquare([16, 18, 16, 14, 12, 12], f_exp=[16, 16, 16, 16, 16, 8]))
