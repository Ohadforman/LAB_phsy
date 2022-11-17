import numpy as np
from eddington import fitting_function
@fitting_function(n=3)
def T2_total_simple(a, x):
    return a[0]   *  (np.exp(-a[1]*(x-a[2])))  