import unittest
from code.hello import cuboid, sum, subtract, square


class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid(2), 8)
        self.assertAlmostEqual(cuboid(1), 1)
        self.assertAlmostEqual(cuboid(0), 0)
        self.assertAlmostEqual(cuboid(5.5), 166.375)
        self.assertAlmostEqual(sum(2, 3), 5)
        self.assertAlmostEqual(subtract(5, 7), -2)
        self.assertAlmostEqual(subtract(0, 0), 0)
        self.assertAlmostEqual(square(0), 0)
        self.assertAlmostEqual(square(-5), 25)
