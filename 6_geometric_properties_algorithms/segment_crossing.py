# so to find it the two segments cross one another we simply copy the point_to_segment code and insert it, will be useful
# and then create 4 equations using determinant 3x3 to calculate if they cross
# I don't know really, now it's just following equations
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


def point_on_segment(a: Point, b: Point, c: Point) -> bool:
    matrix = [[a.x, a.y, 1], [b.x, b.y, 1], [c.x, c.y, 1]]

    if determinant_3_by_3(matrix) != 0:
        return False

    return (
            min(a.x, b.x) <= c.x <= max(a.x, b.x)
            and
            min(a.y, b.y) <= c.y <= max(a.y, b.y)
    )


def segment_crossing(a: Point, b: Point, c: Point, d: Point) -> bool:
    e1 = determinant_3_by_3([[a.x, a.y, 1], [b.x, b.y, 1], [c.x, c.y, 1]])
    e2 = determinant_3_by_3([[a.x, a.y, 1], [b.x, b.y, 1], [d.x, d.y, 1]])
    e3 = determinant_3_by_3([[c.x, c.y, 1], [d.x, d.y, 1], [a.x, a.y, 1]])
    e4 = determinant_3_by_3([[c.x, c.y, 1], [d.x, d.y, 1], [b.x, b.y, 1]])

    return ((e1 * e2 < 0 and e3 * e4 < 0)
            or point_on_segment(a, b, c)
            or point_on_segment(a, b, d)
            or point_on_segment(c, d, a)
            or point_on_segment(c, d, b)
            )


point_a = Point(1, 1)
point_b = Point(5, 5)
point_c = Point(2, 2)
point_d = Point(3, 3)

result = 'Yes' if segment_crossing(point_a, point_b, point_c, point_d) else 'No'
print(f'Is the segments cross one another? {result}')