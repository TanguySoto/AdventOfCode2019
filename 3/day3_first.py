import os

"""
https://adventofcode.com/2019

Day 3 - First puzzle

@author Tanguy Soto
@date 03/12/2019 - Darmstadt
"""


def manhattan_to_central(point):
    """
    Returns the manhattan distance of the point to the central port (point(0,0)).

    :param tuple(int, int) point: the given point
    :return int: the manhattan distance
    """
    return abs(point[0]) + abs(point[1])


def find_closest_intersection_to_central(wire1_pos, wire2_pos):
    """
    Computes every intersection between the 2 wires positions and returns the closest
    one to the central port (point(0,0)).

    :param list[tuple(int, int)] wire1_pos: positions of the first wire
    :param list[tuple(int, int)] wire1_pos: positions of the second wire
    :return tuple(int, int): the intersection point
    """

    wire1_pos_set = set(wire1_pos)
    intersections = [pos for pos in wire2_pos if pos in wire1_pos_set]
    intersections.sort(key=lambda pos: manhattan_to_central(pos))

    return intersections[1] if len(intersections) > 1 else None


def generate_wires_positions(wires_file_abspath):
    """
    Reads the file containng the wires move and generate every positions of the wires.

    :param String wires_file_abspath: path to the file containing the wires moves
    :return list[tuple(int, int)], list[tuple(int, int)]: positions of the first and second wire
    """

    dir_to_vector = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    wires_pos = ([(0, 0)], [(0, 0)])

    with open(wires_file_abspath, 'r') as f:
        wires_path = f.readlines()

        # for each wires
        for i in range(len(wires_path)):
            moves = wires_path[i].strip().split(',')

            # for each move
            for j in range(len(moves)):
                pos_shift = dir_to_vector[moves[j][0]]

                # create each position from previous positions
                wires_pos[i].extend(
                    tuple(
                        [pos_shift[k] + wires_pos[i][-1][k]
                            for k in range(len(pos_shift))]) for l in range(int(moves[j][1:])))
    return wires_pos


if __name__ == '__main__':
    INPUT_FILE_ABSPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "first_input.txt")

    wire1_pos, wire2_pos = generate_wires_positions(INPUT_FILE_ABSPATH)
    closest_intersection = find_closest_intersection_to_central(wire1_pos, wire2_pos)
    answer = manhattan_to_central(closest_intersection)

    print("Day3 - first puzzle answer:\n{}".format(answer))
