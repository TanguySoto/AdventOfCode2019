import os
import math

"""
https://adventofcode.com/2019

Day 1 - Second puzzle

@author Tanguy Soto
@date 03/12/2019 - Darmstadt
"""


def process_module_mass(module_mass):
    """
    Returns the fuel needed for the provided mass.

    :param int module_mass: mass of the module to process
    :return int: fuel needed for this module
    """

    needed_fuel = 0

    while module_mass > 0:
        current_needed_fuel = max(0, module_mass // 3 - 2)
        needed_fuel += current_needed_fuel
        module_mass = current_needed_fuel

    return needed_fuel


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
    INPUT_FILE_ABSPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "second_input.txt")

    answer = process_spacecraft(INPUT_FILE_ABSPATH)

    print("Day1 - second puzzle answer:\n{}".format(answer))
