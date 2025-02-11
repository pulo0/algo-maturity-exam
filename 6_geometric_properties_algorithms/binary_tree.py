import turtle

# simple binary tree fractal, pretty self and explanatory to look at and code wise
# two main branches which go and create small sub-branches, amount of them are rank parameter
def binary_tree(rank: int, length: float):
    turtle.forward(length)

    if rank > 0:
        turtle.left(45)
        binary_tree(rank - 1, length / 2)
        turtle.right(90)
        binary_tree(rank - 1, length / 2)
        turtle.left(45)

    turtle.back(length)

turtle.penup()
turtle.left(90)
turtle.back(360)
turtle.pendown()
turtle.pensize(3)

binary_tree(5, 400)

turtle.done()