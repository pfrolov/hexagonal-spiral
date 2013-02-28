# Hexagonal Sprial #

## How to use ##

#### Calculate the distance ####

    python src/distance.py 19 30

#### Running the tests ####

    nosetests

## Overview ##

Computes the distance between two cells on the hexagonal grid labeled by centered hexagonal numbers. 

The cells are labled by marking an arbitrary cell as number 1, and then labeling the remaining cells in a clockwise fashion.

![Hexagonal grid example](/images/grid.png)

For example, the distance between two cells labeled 19 and 30 is 5. One of the shortest paths connecting the two cells is via the cells 19 - 7 - 6 - 5 - 15 - 30, so you must move five times to adjacent cells to get from 19 to 30.

## Solution ##

The high level description of the algorithm:

1.  Compute coordinates of a cell labeled by a number in the hexagonal coordinate system
2.  Compute the distance between two cells in the hexagonal coordinate system


### Hexagonal coordinate system ###

The hexagonal coordinate system is defined as shown on the image.

![Hexagonal grid with coordinate example](/images/grid_coordinates.png)

### The distance metric ###

The distance between two cell A and B is defined by:

    dx = B.x - A.x;
    dy = B.y - A.y;
    
    if (sign(dx) == sign(dy)) {
        dist = max(abs(dx), abs(dy));
    } else {
        dist = abs(dx) + abs(dy);
    }

### Computing coordinates of a cell ###

The sequence described by the algorithm above is the sequence [A003215](http://oeis.org/A003215 "A003215") of Hex (or centered hexagonal) numbers: 3 * n * (n + 1) + 1 (crystal ball sequence for hexagonal lattice).

Solving the equation 3 * n * (n + 1) + (1 - cell_label) = 0 gives the distance of the cell from the cell labeled by 1 or the center.

To get a position of the cell on its level of the spiral, we subtract the maximum number of a cell on the previous level from the cell label: 

    cell_level_position = cell_label - (3 * (cell_distance - 1) * (cell_distance - 1) + 3 * (cell_distance - 1)  + 1)

It can be used to calculate the cell "diagonal":

    diagonal = ceiling(cell_level_position / cell_distance)

We map six "diagonals" to coordinates (diagonal_coordinates):

    1. (-1, -1)
    2. (-1, 0)
    3. (0, 1)
    4. (1, 1)
    5. (1, 0)
    6. (0, -1)

and to coordinate shifts (diagonal_shift_coordinates):

    1. (1, 0)
    2. (0, -1)
    3. (-1, -1)
    4. (-1, 0)
    5. (0, 1)
    6. (1, 1)

The shift of the cell relative to its "diagonal" is defined as:
    
    diagonal_shift = diagonal * cell_distance - cell_level_position

To calculate cell coordinates:

    cell_coordinates = diagonal_coordinates * cell_distance + diagonal_shift_coordinates * diagonal_shift

    





