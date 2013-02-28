import operator
import argparse
from math import sqrt
from math import ceil

DIAGONAL_COORDINATES = [0, -1, -1, 0, 1, 1, 0]
SHIFT_COORDINATE_UPDATE = [1, 0, -1, -1, 0, 1, 1]

def main():
    parser = argparse.ArgumentParser(description='Compute distance between two integers in the hexagonal grid.')
    parser.add_argument('numbers', metavar='numbers', type=int, nargs=2, help='numbers on the grid')
    args = parser.parse_args()

    number1 = args.numbers[0]
    number2 = args.numbers[1]
    dist = distance(number1, number2)

    print "The distance between {0} and {1} is {2}".format(number1, number2, dist)

def distance(number1, number2):
    """Computes the distance between two numbers
    """

    coord1 = number_to_grid_coord(number1)
    coord2 = number_to_grid_coord(number2)
    return hexagonal_distance(coord1, coord2)


def distance_from_center(number):
    """Computes the distance for a given number from the center

    Computation based on the sequence of Hex (or centered hexagonal) numbers: 3*n*(n+1)+1

    See http://oeis.org/A003215 for details.
    """
    if number == 0:
        return 0
    return int(ceil((-3 + sqrt(-3 + 12 * number)) / 6))


def level_max_number(level):
    """Computes the maximum number on a given level

    Computation based on the sequence of Hex (or centered hexagonal) numbers: 3*n*(n+1)+1
    """

    levelm3 = 3 * level
    return levelm3 * level + levelm3 + 1


def hexagonal_distance(coord1, coord2):
    """Computes the dinstance between two hexagons in the hexagonal coordinate system

    Args:
        coord1: Coordinates of the first hexagon as a tuple.
        coord2: Coordinates of the second hexagon as a tuple.

    Returns:
        An integer distance between two hexagons.

    """

    dx = coord1[0] - coord2[0]
    dy = coord1[1] - coord2[1]

    if ((dx < 0) == (dy < 0)):
        dist = max(abs(dx), abs(dy))
    else:
        dist = abs(dx) + abs(dy)

    return dist

def number_to_grid_coord(number):
    """Convert a number to its coordinates in the hexagonal coordinate system

        Args:
            number: A number assigned to a hexagon

        Returns:
            Coordinates of the number in the hexagonal coordinate system as
            a tuple.
    """

    distance = distance_from_center(number)
    if distance == 0:
        return (0, 0)

    max_number_prev_level = level_max_number(distance -1)
    level_shift = number - max_number_prev_level
    diagonal = int(ceil(level_shift / float(distance)))
    diagonal_shift = diagonal * distance - level_shift

    slice_start = diagonal % 6
    slice_end = diagonal % 6 + 2
    diagonal_coordinates = tuple(DIAGONAL_COORDINATES[slice_start:slice_end])
    diagonal_coordinates = tuple([coord * distance for coord in diagonal_coordinates])

    slice_start = diagonal - 1
    slice_end = diagonal + 1
    diagonal_shift_coordinates = tuple(SHIFT_COORDINATE_UPDATE[slice_start:slice_end])
    diagonal_shift_coordinates = tuple([coord * diagonal_shift for coord in diagonal_shift_coordinates])

    res = tuple(map(operator.add, diagonal_coordinates, diagonal_shift_coordinates))
    res = tuple([int(coord) for coord in res])

    return res


if __name__=='__main__':
    main()
