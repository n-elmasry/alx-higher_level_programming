#!/usr/bin/python3
"""MyInt is a rebel. MyInt has == and != operators inverted"""


class MyInt(int):
    """A class MyInt that inverts == and != operators."""

    def __eq__(self, other):
        """Override equality operator."""
        return int(self) != other

    def __ne__(self, other):
        """Override inequality operator."""
        return int(self) == other
