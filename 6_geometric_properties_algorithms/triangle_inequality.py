# this code just checks whether you can create a triangle if the sides are like given from user
# it's just a mathematics theorem that any side of a triangle has a smaller length to a sum of the other sides
# so basically: a < b + c, b < a +c, c < a + b
# so you put everything to everything as a condition to return and it'll provide bool, either True or False
def triangle(a, b, c):
    return a < b + c and b < a + c and c < a + b

side_a, side_b, side_c = list(map(int, input('Enter all sides of a triangle to check if it can be made: ').split(' ')))
print(triangle(side_a, side_b, side_c))