# so basically it's pretty much the same as the point_line_distance, we use
# (y−yA)(xB−xA)−(yB−yA)(x−xA)=0 this equation to measure if the point belong to a segment (so it needs to equal 0)
# instead of creating dictionaries we create a helper class, point that would have x and y coordinate and from that
# we're going to work a bit
# mainly we'll use a method by Sarrus, using determinant, basically a matrix 3x3, because if you know
# Sarrus rule, we use it we have exactly 3x3 matrix, so that's the function determinant uses, next we just create a
# real matrix with data [A, B, P] p for point and A B are a segment
# so when we will know that a point belonging into a segment from an equation (so it equals 0), we just check whether
# a point is between A and B point, simple, using equation:
# min(xa, xb) <= xp <= max(xa, xb), min(ya, yb) <= yp <= max(ya, yb)
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def determinant_3_by_3(matrix: list) -> int:
    return (matrix[0][0] * matrix[1][1] * matrix[2][2]
            + matrix[1][0] * matrix[2][1] * matrix[0][2]
            + matrix[2][0] * matrix[0][1] * matrix[1][2]
            - matrix[1][0] * matrix[0][1] * matrix[2][2]
            - matrix[0][0] * matrix[2][1] * matrix[1][2]
            - matrix[2][0] * matrix[1][1] * matrix[0][2])


def point_on_segment(a: Point, b: Point, p: Point) -> bool:
    matrix = [[a.x, a.y, 1], [b.x, b.y, 1], [p.x, p.y, 1]]

    if determinant_3_by_3(matrix) != 0:
        return False

    return (
            min(a.x, b.x) <= p.x <= max(a.x, b.x)
            and
            min(a.y, b.y) <= p.y <= max(a.y, b.y)
    )


point_a = Point(1, 1)
point_b = Point(5, 5)
point_p = Point(2, 2)

result = 'Yes' if point_on_segment(point_a, point_b, point_p) else 'No'

print(f'Is the point belong to given segment? {result}')
