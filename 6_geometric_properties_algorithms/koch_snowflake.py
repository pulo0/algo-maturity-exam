import turtle

# so basically we want to create a Koch Snowflake, made out of 4 Koch curves (look at for loop in koch_snowflake method)
# in koch_curve we create a curve, firstly horizontally and then with a for loop we will change direction to create with
# curve a whole big snowflake
def koch_curve(rank, length):
    if rank > 0:
        koch_curve(rank - 1, length / 2)
        turtle.left(60)
        koch_curve(rank - 1, length / 2)
        turtle.right(120)
        koch_curve(rank - 1, length / 2)
        turtle.left(60)
        koch_curve(rank - 1, length / 2)
    else:
        turtle.forward(length)

def koch_snowflake(rank, length):
    for _ in range(3):
        koch_curve(rank, length)
        turtle.right(120)

turtle.speed(0)
turtle.penup()
turtle.back(350)
turtle.pendown()

koch_snowflake(3, 100)

turtle.done()