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


def point_in_triangle(a: Point, b: Point, c: Point, p: Point):
    e1 = determinant_3_by_3([[a.x, a.y, 1], [b.x, b.y, 1], [p.x, p.y, 1]])
    e2 = determinant_3_by_3([[b.x, b.y, 1], [c.x, c.y, 1], [p.x, p.y, 1]])
    e3 = determinant_3_by_3([[c.x, c.y, 1], [a.x, a.y, 1], [p.x, p.y, 1]])
    if e1 * e2 < 0 or e1 * e3 < 0:
        return False
    return True

point_a = Point(1, 1)
point_b = Point(5, 5)
point_c = Point(2, 2)
point_p = Point(3, 3)

result = 'Yes' if point_in_triangle(point_a, point_b, point_c, point_p) else 'No'
print(f'Is a point in a triangle (so just create a three vector which will be sides)? {result}')