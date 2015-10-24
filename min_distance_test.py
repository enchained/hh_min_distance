import unittest
from min_distance import min_dist


class FindMinDistTests(unittest.TestCase):
    """
    unit-tests to cover provided example cases data
    """
    def test_from_example(self):
        points = [(10, 10), (20, 10), (20, 15)]
        self.assertEqual(min_dist(points), 5)

if __name__ == '__main__':
    unittest.main()
