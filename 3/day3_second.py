import os
import day3_first

"""
https://adventofcode.com/2019

Day 3 - Second puzzle

@author Tanguy Soto
@date 03/12/2019 - Darmstadt
"""


def find_fewest_steps_intersection(wire1_pos, wire2_pos):
    """
    Finds the intersection of the 2 wires that has the lowest total number of steps.

    :param list[tuple(int, int)] wire1_pos: positions of the first wire
    :param list[tuple(int, int)] wire1_pos: positions of the second wire
    :return int: the total number of steps of the found intersection
    """

    wire1_pos_set = set(wire1_pos)
    intersections = [pos for pos in wire2_pos if pos in wire1_pos_set]

    intersections.sort(key=lambda pos: wire1_pos.index(pos) + wire2_pos.index(pos))

    return wire1_pos.index(intersections[1]) + wire2_pos.index(intersections[1]) if len(intersections) > 1 else None


if __name__ == '__main__':
    INPUT_FILE_ABSPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "second_input.txt")

    wire1_pos, wire2_pos = day3_first.generate_wires_positions(INPUT_FILE_ABSPATH)
    answer = find_fewest_steps_intersection(wire1_pos, wire2_pos)

    print("Day3 - second puzzle answer:\n{}".format(answer))
