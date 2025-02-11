import turtle

# Sierpinski Square is also a fractal, similar to triangle from Sierpinski, but as a base we use squares
# so basically an if statement is used for filling the small squares and nested loops are for maneuvering around
# a bigger square that we'll produce as an end result
def sierpinski_square(rank, length):
    if rank == 0:
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(length)
            turtle.left(90)
        turtle.end_fill()
        return

    for _ in range(4):
        for _ in range(2):
            turtle.forward(length/3)
            sierpinski_square(rank-1, length/3)
        turtle.forward(length/3)
        turtle.left(90)

turtle.color('blue')
turtle.penup()
turtle.back(200)
turtle.pendown()

sierpinski_square(3, 300)

turtle.done()