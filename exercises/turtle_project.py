"""Exercise 05: Turtle Scene Project :) !"""

__author__ = "730489972"

from turtle import Turtle, colormode, done 
bart: Turtle = Turtle()  # Using a fun name to define turtle like the tutorial
colormode(255)


def house(bart: Turtle) -> None:
    """Using a function to make a house."""
    bart.penup()
    bart.goto(-50, -100)  # Telling the pen where to start the drawing
    bart.pendown()
    bart.color(235, 107, 52)
    bart.begin_fill()  # Filling the square of the house with an orangey color
    i: int = 0
    while (i < 4): 
        # Drawing a line 4 times in order to make each side of a square
        bart.forward(100)
        bart.left(90)
        i = i + 1
    bart.end_fill()


def roof(bart: Turtle) -> None:
    """Creating the roof by drawing a triangle on top of the square."""
    bart.penup()
    bart.goto(-60, 0)
    bart.pendown()
    bart.color(235, 61, 52)
    bart.begin_fill()  # Filling the triangle with a red-ish color
    i: int = 0
    while (i < 3):  # While is less than or equal to 3, create 3 lines to make a triangular roof
        bart.forward(120)
        bart.left(120)
        i = i + 1
    bart.end_fill()


def draw_tree(bart: Turtle) -> None: 
    """Drawing a tree using a square and a triangle."""
    bart.penup()
    bart.goto(40, -100)
    bart.pendown()
    bart.pencolor(82, 52, 23)  # Using brown for the tree trunk; using a darker color for the outline of the tree
    bart.color(99, 64, 28)
    bart.begin_fill()
    i: int = 0
    while (i < 3):  # Using while loops to create a triangle
        bart.forward(20)
        bart.left(120)
        i = i + 1
    bart.end_fill()


def draw_bush(bart: Turtle) -> None:
    """Drawing the tree part to the trunk to break up long function."""
    bart.penup()
    bart.goto(35, -80)
    bart.pendown()
    bart.color(23, 82, 43)  # Using rgb throughout this whole code because I like specific colors
    bart.begin_fill()
    i: int = 0
    while i < 4: 
        bart.forward(30)
        bart.left(90)
        i = i + 1
    bart.end_fill()


def flower(bart: Turtle, x: float, y: float) -> None:
    """Creating flowers with different x and y inputs to modify the location of flower placements."""
    bart.penup()
    bart.goto(x, y)
    bart.pendown()
    bart.color(186, 128, 207)  # rgb for a lavendar color
    bart.begin_fill()
    bart.circle(8)  # drawing circle as the "flower" and the value inside the paranthesis affects the size of the circle
    bart.end_fill()


def flower_stem(bart: Turtle, x: float, y: float) -> None:
    """Creating the stem to the flowers above."""
    bart.color(74, 130, 65)  # rgb for a green color
    bart.penup()
    bart.goto(x, y - 7)
    bart.pendown()
    bart.begin_fill()
    bart.goto(x, y - 20)
    bart.goto(x + 3, y - 25)  # drawing the stem of the flower and it varies with the different x and y inputs 
    bart.goto(x - 3, y - 25)
    bart.goto(x, y - 20)
    bart.end_fill


def hill(bart: Turtle) -> None:
    """Creating a green landscape or hill for the house to sit upon."""
    bart.penup()
    bart.goto(-300, -100)
    bart.pendown()
    bart.color(97, 186, 84)
    bart.begin_fill
    i: int = 0
    while i < 2:  # using while loops to create a rectangular landscape
        bart.forward(600)
        bart.right(90)
        bart.forward(150)
        bart.right(90)
        i = i + 1
    bart.end_fill()


def main() -> None:
    """Putting all of the functions together - the entrypoint of my scene."""
    bart.speed(6)   # speed can vary from 1 (slow) and 10 (fast) but i prefer a moderate speed
    house(bart)
    roof(bart)
    draw_tree(bart)
    draw_bush(bart)
    flower(bart, -10, -90)  # the flowers have a x and y input unlike the rest of the functions
    flower_stem(bart, -10, -90)
    flower(bart, 10, -90)
    flower_stem(bart, 10, -90)
    flower(bart, 20, -95)
    flower_stem(bart, 20, -95)
    hill(bart)
    done()


if __name__ == "__main__":  # calling on the main function that goes through and assembles the other functions
    main()