'''main.py

This module contains the main program.

@author: Fang pongkit
@date:2022-12-12
@version: 1.0
'''
import numpy as np
import matplotlib.pyplot as plt
from tools import *


def main():
    '''main

    This function runs the main program.

    @return: None
    '''
    # Generate a list of values from 0 to 1 with a step size of 1e-4
    region = generate_region(0, 1, 1e-4)
    print(len(region))
    # generate a list of Brownian increments
    B_list = []
    for i in range(len(region)):
        B_list.append(generate_increment(0.01))
    print('generate a list of Brownian increments')
    # Solve the second problem
    x0 = 1
    alpha = 0.001
    v = 0.1
    X_list = []
    for s in range(1,10001):
        X_list.append(generate_solution_pro2(alpha, v, x0, B_list, s))
    # plot the graph
    print('plot the graph')
    plt.plot(region, X_list)
    plt.show()


if __name__ == '__main__':
    main()