# Problem 13:
#     Large Sum
#
# Description:
#     Starting in the top left corner of a 2×2 grid,
#       and only being able to move to the right and down,
#       there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

from math import comb


def main(w, h):
    """
    Returns the number of distinct paths through a `w`×`h` rectangular grid,
        starting in the top-left corner,
        ending in the bottom-right corner,
        only having steps down or right.

    Args:
        w (int): Natural number
        h (int): Natural number

    Returns:
        Number of down-right lattice paths through w×h grid.
    """
    assert type(w) == int and w > 0
    assert type(h) == int and h > 0

    # Paths are always w+h steps in total,
    #   making w steps to the right,
    #   and h steps down.
    # Count the number of all such sequences.
    return comb(w+h, w)


if __name__ == '__main__':
    width = int(input('Enter a grid width:  '))
    height = int(input('Enter a grid height: '))
    paths = main(width, height)
    print('Number of paths from top-left to bottom-right of {}×{} grid:'.format(width, height))
    print('  {}'.format(paths))
