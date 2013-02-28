# Hexagonal Sprial #

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
