"""
Square module that create a Square class
inherited from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represent a square inherited from the Reactangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square class.
        Args:
            size (int): size of the new Square.
            x (int): x coordinate of the new Square.
            y (int): y coordinate of the new Square.
            id (int): identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for both width and height which
        are the same in this case
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the
        square in the format:
        [Square] (<id>) <x>/<y> - <size>

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
