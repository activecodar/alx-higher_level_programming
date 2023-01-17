import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle(10, 20)

    def test_width_getter(self):
        self.assertEqual(self.r.width, 10)

    def test_width_setter(self):
        self.r.width = 30
        self.assertEqual(self.r.width, 30)

    def test_height_getter(self):
        self.assertEqual(self.r.height, 20)

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

if __name__ == '__main__':
    unittest.main()
