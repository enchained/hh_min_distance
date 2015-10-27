import unittest
from min_distance import min_dist, distance
from random import randrange


def bruteforce_md(pts):
    """
    Find minimum distance between 2 points from provided set,
    using brute-force algorithm.

    Args:
        pts (list): list of points as tuples with 2 integer coordinates each.
    Returns:
        min_d (float): minimum distance between closest pair of points.
    """
    min_d = float('inf')  # infinity

    for p in pts:
        for q in pts:
            if not (p is q):
                dist = distance(p, q)
                if dist < min_d:
                    min_d = dist
    return min_d


def gen_points(n):
    # Returns n random points as list of n tuples with 2 integer coordinates.
    points = []

    for i in range(n):
        points.append((randrange(-50, 51), randrange(-50, 51)))

    return points


class FindMinDistTests(unittest.TestCase):
    """
    Unit-tests to cover provided example cases data
    and check improved algorithm correctness.
    """
    def test_from_example(self):
        points = [(10, 10), (20, 10), (20, 15)]
        self.assertEqual(min_dist(points), 5)

    def test_div_n_conq(self):
        for i in range(100):
            # Generate random points set
            n = randrange(1, 101)
            points = gen_points(n)

            # Compare bruteforce vs divide and conquer solution
            self.assertEqual(bruteforce_md(points), min_dist(points))


if __name__ == '__main__':
    unittest.main()
