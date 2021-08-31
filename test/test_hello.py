 import unittest
 
 from hello import hello
 class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid(2),8)
        self.assertAlmostEqual(cuboid(1),1)
        self.assertAlmostEqual(cuboid(0),0)
        self.assertAlmostEqual(cuboid(5.5),166.375)
