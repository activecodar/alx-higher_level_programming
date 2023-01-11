#!/usr/bin/python3
"""My int module"""


class MyInt(int):
    """Invert int ops == and !=."""

    def __eq__(self, other):
        """Override == op with !=."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Override != op with ==."""
        return int.__eq__(self, other)
