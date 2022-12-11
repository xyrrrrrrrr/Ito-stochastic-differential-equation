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
    x = generate_region(0, 1, 1e-4)
    # print(len(x))
    current_y_state = 0
    y_state = []
    for i in range(len(x)):
        current_y_state += generate_increment(0.01)
        y_state.append(current_y_state)
    # plot the graph
    plt.plot(x, y_state)
    plt.show()




if __name__ == '__main__':
    main()