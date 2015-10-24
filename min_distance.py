import sys
import math


def min_dist(pts):
    """
    pts: list of points as tuples with 2 integer coordinates each
    ---
    This function finds min distance between 2 points from provided set.
    ---
    returns: minimum distance
    """
    min_d = float('inf')  # infinity

    for p in pts:
        for q in pts:
            if not (p is q):
                dist = math.hypot(q[0] - p[0], q[1] - p[1])
                if dist < min_d:
                    min_d = dist
    return min_d


def main(lines):
    points = []
    # read points
    for line in lines:
        tup = tuple(int(n) for n in line.strip().split())
        points.append(tup)
    if not points:
        print "No points were provided"
        return

    min_d = min_dist(points)

    # string formatting for print
    if min_d.is_integer():
        print_d = str(int(min_d))
    else:
        print_d = "{0:.2f}".format(min_d)

    # print solution
    for p in points:
        print p
    print "Minimum distance between points is " + print_d


if __name__ == '__main__':
    # read file
    if len(sys.argv) > 1:
        try:
            filename = sys.argv[1]
            with open(filename, 'r') as input_file:
                lines = input_file.readlines()
                main(lines)
        except IOError as e:
            # in case no such file exist
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
    else:
        print "Error: input file was not provided"
        print "Please run program with text file as an argument"
