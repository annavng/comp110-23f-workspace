"""Testing out Points."""

from lessons.CQ07.make_point import Point

my_point: Point = Point(1.0, 2.0)
my_point.scale_by(5)
print(my_point.y)
my_point.scale(2)
print(my_point.x)