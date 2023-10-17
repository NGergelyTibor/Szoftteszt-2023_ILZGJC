import unittest
from holdjaro import Holdjaro

class TestHoldjaro(unittest.TestCase):
    def test_forward_movement(self):
        holdjaro = Holdjaro(0, 0, 'N', [], 100)
        result = holdjaro.move('f')
        self.assertEqual(result, (0, 1, 'N'))

if __name__ == '__main__':
    unittest.main()
