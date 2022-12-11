'''tools.py

This module contains a collection of tools for use in the
main program.

@author: Fang pongkit
@date:2022-12-12
@version: 1.0
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def generate_region(min, max, step):
    '''generate_region

    This function generates a list of values from min to max
    with a step size of step.

    @param min: the minimum value of the list
    @param max: the maximum value of the list
    @param step: the step size of the list

    @return: a list of values from min to max with a step size of step
    '''
    return np.arange(min, max, step)

def generate_increment(sigma_2):
    '''generate_increment

    This function generates a increment according to
    the given variance.

    @param sigma_2: the variance of the increment

    @return: a increment
    '''
    return np.random.normal(0, sigma_2)

def generate_solution_pro2(alpha, v, X0, B_list, t):
    '''generate_solution_pro2
    
    This function generates the solution of the second problem.

    @param alpha: the parameter alpha
    @param v: the parameter v
    @param x0: the initial value of x
    @param B_list: the list of Brownian increments
    @param t: the time in range of 1 to 10000

    @return: X(t)
    '''
    count = 0
    for s in range(t):
        count += B_list[s] * np.exp(alpha * s)    
    
    Xt = X0 * np.exp(-alpha * t) + v * (1 - np.exp(-alpha * t)) + count * np.exp(-alpha * t)
    return Xt