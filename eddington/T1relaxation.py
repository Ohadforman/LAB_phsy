import numpy as np
from eddington import fitting_function
@fitting_function(n=3)
def T1relaxation(a, x):
    return a[0]*(1-2*np.exp(-a[1]*(x-a[2])))