# import libraries
import numpy as np

# constants
Z0=0 + 0j  # starting value of z0
NITERS = 100  # number of iterations to use in the z_i equation iteration

# define the z_{i + 1} equation to iterate over
def quad_map_colouring(c, z0=Z0, niters=NITERS):
    """
    quad_map_colouring(c, z0=Z0, niters=NITERS):
    
    Determines at what iteration a given complex number c results in z_i diverging for the quadratic map 
    z_{i + 1} = z_i + c for some starting condition z_0 (by default z_0 = 0), or returns -1 if z_i does not diverge even after the maximum number of iterations is computed (by default 100), assuming that z_i is bounded for that value of c.
    
    Parameters:
    ---------
    c: complex
    Value for which to compute the quadratic map z_{i + 1} = z_i + c and determine whether it diverges
    z0 = Z0: complex, default
    Initial condition z_0 for the quadratic map. Set by default to z_0 = 0 (in which case it produces the Mandelbrot set).
    niters=NITERS: int, default
    Maximum number of iterations for the quadratic map to determine whether c results in convergence. Set by default to 100

    Returns:
    ---------
    i: int
    Iteration number at which the quadratic map diverges for the given value of c (either the magnitude of the real or imaginary part of z_i becomes larger than 2. If z_i stays bounded even after the maximum number of iterations is reached, returns -1 to represent boundedness.
    """
    zi = np.array([z0] * niters)  # initialize the zi array
    
    # loop that iterates to see if quadratic map diverges
    for i in range(1, niters):  # start at 1 since 0th element is z0
        zi[i] = (zi[i - 1] ** 2) + c  # iterative step
        if np.abs(zi[i].real) > 2. or np.abs(zi[i].imag) > 2.:  # compares zi to zi-1
            return i  # if diverges after a certain number of iterations, 
                    # return the iteration number at which it diverges
    # if hasn't diverged after n iterations, return -1
    return -1  # -1 represents convergence