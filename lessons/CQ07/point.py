"""Creating a Point Class."""


from __future__ import annotations


class Point:
    """Attributes."""
    x: float = 0.0
    y: float = 0.0

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Reestablishing values."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Belongs to the point class and mutates a Point."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creating a new point."""
        new_x = self.x * factor
        new_y = self.y * factor
        return Point(new_x, new_y)
    
    def __str__(self) -> str:
        """Returning x and y values."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Multipying point with a factor."""
        new_x = self.x * factor
        new_y = self.y * factor
        return Point(new_x, new_y)
    
    def __add__(self, factor: int | float) -> Point:
        """Overloading the addition operator."""
        new_x = self.x + factor
        new_y = self.y + factor
        return Point(new_x, new_y)
