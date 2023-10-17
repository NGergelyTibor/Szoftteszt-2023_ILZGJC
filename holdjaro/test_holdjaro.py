import unittest
from holdjaro import Holdjaro

class TestHoldjaro(unittest.TestCase):
    def test_forward_movement(self):
        holdjaro = Holdjaro(0, 0, 'N', [], 100)
        result = holdjaro.move('f')
        self.assertEqual(result, (0, 1, 'N'))

    def test_backward_movement(self):
        holdjaro = Holdjaro(0, 0, 'E', [], 100)
        result = holdjaro.move('b')
        self.assertEqual(result, (1, 0, 'E'))

    def test_turn_left(self):
        holdjaro = Holdjaro(0, 0, 'N', [], 100)
        result = holdjaro.move('l')
        self.assertEqual(result, (0, 0, 'W'))

    def test_turn_right(self):
        holdjaro = Holdjaro(0, 0, 'E', [], 100)
        result = holdjaro.move('r')
        self.assertEqual(result, (0, 0, 'S'))
        
    def test_boundary_handling(self):
        obstacles = [(10, 10), (20, 30)]
        planet_radius = 50
        holdjaro = Holdjaro(45, 0, 'E', obstacles, planet_radius)
        result = holdjaro.move('f')
        self.assertEqual(result, (50, 0, 'E'))

if __name__ == '__main__':
    unittest.main()
