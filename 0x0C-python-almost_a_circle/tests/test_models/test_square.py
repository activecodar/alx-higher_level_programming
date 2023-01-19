import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.r = Square(10)
        self.sq_update = Square(4, 6, 7, 8)

    def test_width_getter(self):
        self.assertEqual(self.r.width, 10)

    def test_width_setter(self):
        self.r.width = 30
        self.assertEqual(self.r.width, 30)

    def test_height_getter(self):
        self.assertEqual(self.r.height, 10)

    def test_height_setter(self):
        self.r.height = 40
        self.assertEqual(self.r.height, 40)

    def test_x_getter(self):
        self.assertEqual(self.r.x, 0)

    def test_x_setter(self):
        self.r.x = 10
        self.assertEqual(self.r.x, 10)

    def test_y_getter(self):
        self.assertEqual(self.r.y, 0)

    def test_y_setter(self):
        self.r.y = 20
        self.assertEqual(self.r.y, 20)
    
    def test_area(self):
        self.assertEqual(self.r.area(), 100)

    def test_x_validation(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Square(10, x="0")
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r = Square(10, x=-1)

    def test_y_validation(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Square(10, 20, y="0")
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r = Square(10, 20, y=-1)


if __name__ == '__main__':
    unittest.main()
