import sys
import math
from operator import itemgetter


def min_dist(pts):
    """
    Find minimum distance between 2 points from provided set,
    using divide and conguer algorithm based on:
    https://en.wikipedia.org/wiki/Closest_pair_of_points_problem

    Args:
        pts (list): list of points as tuples with 2 integer coordinates each.
    Returns:
        min_d (float): minimum distance between closest pair of points.
    """
    # Sort point sets by x and y values
    ptsX = sorted(pts, key=itemgetter(0))
    ptsY = sorted(pts, key=itemgetter(1))

    # Initial call to recursive md function
    min_d = md(ptsX, ptsY)
    return min_d


def distance(p, q):
    # Returns distance between 2 points as float.
    return math.hypot(q[0] - p[0], q[1] - p[1])


def md(ptsX, ptsY):
    """
    Recursively calculates sallest distance (d) among minimum distances
    between points in left and right (d1, d1),
    and between points in the middle in range of that distance d (dY).

    Args:
        ptsX, ptsY (list): list of points as tuples with 2 integer coordinates.
        Sorted by X or Y coordinate. Can contain from 1 to n points each.
    Returns:
        min(d, min_candidates(dY, d)) (float): minimum distance
        between closest pair of points.
    """
    n = len(ptsX)
    # Get middle index of the list
    mid = n/2

    if n == 1:
        return float('inf')  # infinity
    elif n == 2:
        return distance(ptsX[0], ptsX[1])

    # Get left and right half of sorted pts sets
    ptsYL = []
    ptsYR = []
    left_side = {'x': ptsX[:mid], 'y': ptsYL}
    right_side = {'x': ptsX[mid:], 'y': ptsYR}

    for p in ptsY:
        if p in left_side['x']:
            ptsYL.append(p)
        elif p in right_side['x']:
            ptsYR.append(p)

    # Get min dist between points on each half
    d1 = md(left_side['x'], left_side['y'])
    d2 = md(right_side['x'], right_side['y'])
    # Get smallest delta distance
    d = min(d1, d2)

    """
    There is still a chance of a distance smaller than delta (d),
    because we didn't get dist between any left side point vs right side one.
    However we do not need to check every left/right points pair.
    we need to check only those within the delta distance from the middle.
    """
    # dY - points in ptsY within the delta distance from the middle.
    # Last candidates for minimal distance.
    dY = []
    for (x, y) in ptsY:
        # If x coordinate lays in range d from the middle,
        # it should be checked.
        if abs(x - ptsX[mid][0]) < d:
            dY.append((x, y))
    return min(d, min_candidates(dY, d))


def min_candidates(pts, d):
    """
    Check the filnal candidates for minimum distance.

    Args:
        pts (list): list of points as tuples with 2 integer coordinates.
        Were selected as candidates for min dist, as dY.
    Returns:
        min_d: final result of minimum distance
        between closest pair of points.
    """
    min_d = d
    # For every point check distance to other points in list
    for i, (x, y) in enumerate(pts):
        for j in range(i+1, len(pts)):
            # If distance between point y'coords < min_d
            # and distance between point < min_d
            if (pts[j][1] - pts[i][1]) < min_d and \
                distance(pts[i], pts[j]) < min_d:

                min_d = distance(pts[i], pts[j])

    return min_d


def main(lines):
    points = []
    # Read points
    for line in lines:
        tup = tuple(int(n) for n in line.strip().split())
        points.append(tup)
    if not points:
        print "No points were provided"
        return

    min_d = min_dist(points)

    # String formatting for print
    if min_d.is_integer():
        print_d = str(int(min_d))
    else:
        print_d = "{0:.2f}".format(min_d)

    # Print solution
    for p in points:
        print p
    print "Minimum distance between points is " + print_d


if __name__ == '__main__':
    # Read file
    if len(sys.argv) > 1:
        try:
            filename = sys.argv[1]
            with open(filename, 'r') as input_file:
                lines = input_file.readlines()
                main(lines)
        except IOError as e:
            # In case no such file exist
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
    else:
        print "Error: input file was not provided"
        print "Please run program with text file as an argument"
