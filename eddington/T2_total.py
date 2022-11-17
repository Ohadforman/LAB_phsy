import numpy as np
from eddington import fitting_function
@fitting_function(n=4)
def T2_total(a, x):
    return a[0]   *  (np.exp(-a[1]*(x-a[2])))   *   (1-np.exp(-a[3]*(x-a[2])))