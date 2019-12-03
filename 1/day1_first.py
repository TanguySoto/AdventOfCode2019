import os
import math

"""
https://adventofcode.com/2019

Day 1 - First puzzle

@author Tanguy Soto
@date 03/12/2019 - Darmstadt
"""


def process_module_mass(module_mass):
    """
    Returns the fuel needed for the provided mass.

    :param int module_mass: mass of the module to process
    :return int: fuel needed for this module
    """
    
    return max(0, module_mass // 3 - 2)

def process_spacecraft(spacecraft_file_abspath):
    """
    Returns the total fuel needed for the spacecraft.

    :param String: absolute path to the file containing the spacecraft module's masses
    :return int: the fuel needed
    """
    
    total_fuel = 0
    with open(spacecraft_file_abspath, 'r') as f:
        for mass in f.readlines():
            total_fuel += process_module_mass(int(mass))

    return total_fuel

if __name__ == '__main__':
    INPUT_FILE_ABSPATH = os.path.abspath("first_input.txt")

    answer = process_spacecraft(INPUT_FILE_ABSPATH)

    print("Day1 - first puzzle answer:\n{}".format(answer))