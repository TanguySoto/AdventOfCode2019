import os
import math

"""
https://adventofcode.com/2019

Day 2 - First puzzle

@author Tanguy Soto
@date 03/12/2019 - Darmstadt
"""


def process_opcode(opcode, intput1, intput2):
    """
    Process the given opcode with provide inputs.

    :param int opcode: the code, either 1 or 2
    :param int intput1: the first input
    :param int intput2: the second input
    :return int: intput1 + intput2 if opcode == 1 else intput1 * intput2
    """

    return intput1 + intput2 if opcode == 1 else intput1 * intput2


def process_program(program_file_abspath):
    """
    Process the given IntCode program.

    :param String: absolute path to the file containing IntCode program
    :return int: position 0 of the program once processed
    """

    program = []
    with open(program_file_abspath, 'r') as f:
        program = [int(v) for v in f.readline().split(',')]

    curr_index = 0
    while program[curr_index] != 99 and curr_index < len(program):
        program[program[curr_index + 3]] = process_opcode(program[curr_index],
                                                          program[program[curr_index + 1]],
                                                          program[program[curr_index + 2]])
        curr_index += 4

    return program[0]


if __name__ == '__main__':
    INPUT_FILE_ABSPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "first_input.txt")

    answer = process_program(INPUT_FILE_ABSPATH)

    print("Day2 - first puzzle answer:\n{}".format(answer))
