from math import sqrt

# in this algorithm we're just calculating distance between a point and a line
# (in this case we create two points that would be our line and create a vector, meaning ab)
# but all in all this is a part of greater equation, an equation of a line going through two points:
# (y−yA)(xB−xA)−(yB−yA)(x−xA)=0, this is basically a whole equation that we're using for another equation
# (making the b(y-yA) - a(x-xA), stripping simply (xB-xA) and (yB-yA) to b and a respectively)
# for point-line distance, instead of linear function we are using two points line equation in the numerator
# and that's it
def point_line_distance(line_point_1: dict, line_point_2: dict, point):
    a = line_point_2['y'] - line_point_1['y']
    b = line_point_2['x'] - line_point_1['x']

    return abs(b * (point['y'] - line_point_1['y']) - a * (point['x'] - line_point_1['x'])) / sqrt(a*a + b*b)

l_point_1 = {'x': -3, 'y': -4}
l_point_2 = {'x': 4, 'y': 1}
p = {'x': 1, 'y': 1}

print(point_line_distance(l_point_1, l_point_2, p))
