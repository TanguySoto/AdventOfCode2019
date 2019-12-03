import os
import day2_first

"""
https://adventofcode.com/2019

Day 2 - Second puzzle

@author Tanguy Soto
@date 03/12/2019 - Darmstadt
"""


def find_inputs(program_file_abspath, expected_output):
    """
    Find with brute force the inputs (verb and noun) of the given program that
    produce the expected output.

    :param String program_file_abspath: path to the file containing the program
    :param int expected_output: output the program has to produced
    :return (int[0-100], int[0-100]): (verb, noun) that produced the expected output,
                                      None if no combination produced the correct value
    """

    for noun in range(100):
        print(".", end="", flush=True)

        for verb in range(100):
            program = day2_first.load_program(program_file_abspath, noun, verb)

            if day2_first.process_program(program) == expected_output:
                return noun, verb

    return None


if __name__ == '__main__':
    INPUT_FILE_ABSPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "second_input.txt")

    inputs = find_inputs(INPUT_FILE_ABSPATH, 19690720)
    answer = 100 * inputs[0] + inputs[1]

    print("\nDay2 - Second puzzle answer:\n{}".format(answer))
