def f(x: float) -> float:
    # for quadratic function x^2 + 2x
    return x * x * 2 * x

# so to bring up some sort of the introduction, numerical integration is calculating areas beneath the chart in given range
# [a, b] precisely. So we can either calculate areas of the rectangle or trapeze, because there are two methods
# amount in each function refers to amount of figures that will be crammed beneath the chart
# and then iterate through amount to calculate each and every figure of a given method

# Time complexity: O(n)
def rectangle_method(a: int, b: int, amount: int) -> float:
    # initiating firstly variable
    # finding a width of a rectangle by average of range's spectrum
    # and give current_point to go to at the start of a range (so 'a')
    rectangle_width = (b - a) / 2
    current_point = a
    area = 0

    # iterate through all rectangles
    for i in range(amount):
        # scim through to another point with rectangle_with because we already have one side counted of a rectangle
        # height is fascinating because we are using y-axis asymptote of a function, so just calculating this function
        # for a given point that we have right now (I think, again, I might say everything out of my ass)
        # and calculating rectangle area and viola, iterate through all and done (area is a*b simply)
        current_point += rectangle_width
        rectangle_height = f(current_point)
        area += rectangle_height * rectangle_width

    return area

# Time complexity: O(n)
def trapezes_method(a: int, b: int, amount: int) -> float:
    # similar to rectangle but this time with trapeze
    # and for area we want ((a+b)*h) / 2
    # and height is a perfect way to start because it's horizontal, just like width for rectangle
    trapezes_height = (b - a) / 2
    current_point = a
    area = 0

    for i in range(amount):
        # we want two sides of a trapeze so first one is the one before jump of a point and second is after
        # also using y-axis asymptotes
        # and area is a simple area for trapeze
        trapezes_side_one = f(current_point)
        current_point += trapezes_height
        trapezes_side_two = f(current_point)
        area += ((trapezes_side_two + trapezes_side_one) * trapezes_height) / 2

    return area

a_var = 10
b_var = 20
n = 1
print(f'Rectangle method: {rectangle_method(a_var, b_var, n)}')
print(f'Trapezes method: {trapezes_method(a_var, b_var, n)}')
