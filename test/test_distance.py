import unittest
import distance

class DistanceTest(unittest.TestCase):

    def test_distance_from_center(self):
        self.assertEqual(0, distance.distance_from_center(1))

        self.assertEqual(1, distance.distance_from_center(2))
        self.assertEqual(1, distance.distance_from_center(7))

        self.assertEqual(2, distance.distance_from_center(8))
        self.assertEqual(2, distance.distance_from_center(19))

        self.assertEqual(3, distance.distance_from_center(20))
        self.assertEqual(3, distance.distance_from_center(37))

    def test_level_max_number(self):
        self.assertEqual(1, distance.level_max_number(0))
        self.assertEqual(7, distance.level_max_number(1))
        self.assertEqual(19, distance.level_max_number(2))
        self.assertEqual(37, distance.level_max_number(3))

    def test_hexagonal_distance(self):
        coor1 = (0, 0)
        coor3 = (-1, 0)
        coor5 = (1, 1)
        coor12 = (-1, 1)
        coor13 = (0, 2)
        coor19 = (0, -2)
        coor30 = (2, 3)

        self.assertEqual(0, distance.hexagonal_distance(coor1, coor1))

        self.assertEqual(1, distance.hexagonal_distance(coor1, coor5))
        self.assertEqual(1, distance.hexagonal_distance(coor5, coor1))

        self.assertEqual(2, distance.hexagonal_distance(coor3, coor13))
        self.assertEqual(2, distance.hexagonal_distance(coor13, coor3))

        self.assertEqual(4, distance.hexagonal_distance(coor12, coor19))
        self.assertEqual(4, distance.hexagonal_distance(coor19, coor12))

        self.assertEqual(5, distance.hexagonal_distance(coor19, coor30))
        self.assertEqual(5, distance.hexagonal_distance(coor30, coor19))

    def test_number_to_grid_coord(self):
        self.assertEqual((0, 0), distance.number_to_grid_coord(1))
        self.assertEqual((-1, 0), distance.number_to_grid_coord(3))
        self.assertEqual((1, 1), distance.number_to_grid_coord(5))
        self.assertEqual((-1, -2), distance.number_to_grid_coord(8))
        self.assertEqual((-2, -2), distance.number_to_grid_coord(9))
        self.assertEqual((-1, 1), distance.number_to_grid_coord(12))
        self.assertEqual((0, 2), distance.number_to_grid_coord(13))
        self.assertEqual((2, 0), distance.number_to_grid_coord(17))
        self.assertEqual((0, -2), distance.number_to_grid_coord(19))
        self.assertEqual((2, 3), distance.number_to_grid_coord(30))
        self.assertEqual((3, 2), distance.number_to_grid_coord(32))
        self.assertEqual((3, 1), distance.number_to_grid_coord(33))
        self.assertEqual((3, -1), distance.number_to_grid_coord(58))
        self.assertEqual((-5, -3), distance.number_to_grid_coord(68))
        self.assertEqual((-5, 0), distance.number_to_grid_coord(71))

    def test_distance(self):
        self.assertEqual(0, distance.distance(1, 1))

        self.assertEqual(1, distance.distance(1, 3))
        self.assertEqual(1, distance.distance(3, 1))

        self.assertEqual(1, distance.distance(1, 5))
        self.assertEqual(1, distance.distance(5, 1))

        self.assertEqual(2, distance.distance(3, 13))
        self.assertEqual(2, distance.distance(13, 3))

        self.assertEqual(4, distance.distance(12, 19))
        self.assertEqual(4, distance.distance(19, 12))

        self.assertEqual(5, distance.distance(19, 30))
        self.assertEqual(5, distance.distance(30, 19))



if __name__=='__main__':
    unittest.main()
