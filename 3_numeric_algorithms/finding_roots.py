# so basically in this algorithm we want to find a zero (root) of a function between a and b
# where 'a' is a left side of a section and 'b' is a right side
# precision is just like in Newton Raphson method a boundary to which function will recursively iterate upon to which we
# want to find this root, zero

# firstly, it's called Bisection Method

# f function is just a helper function to put in it functions,
# for example in my code, I'm using x^3 - 3x^2 + 2x - 6 polynomial as a function that I want to grab a root from
# it uses also Horner's schema (from return...)
# also each and every function needs to be float (that's why -> float notation) because there a ton of dividing to messy
# non integer number that Python's interpreter would go berserk
def f(x: float) -> float:
    return x * (x * (x - 3) + 2) - 6

# Time complexity: O(log n)
def roots(a: float, b: float, precision: float) -> float:
    # that's just a basic check, putting into x our ranges so a and b and if it'll equal zero then it'll be a root of a
    # function, simple (Bezout's Formula, note: I might say things out of my ass, I'm not so good at math)
    if f(a) == 0.0: return a
    if f(b) == 0.0: return b

    # calculating middle between the range, using arithmetic average,
    # and it'll divide the range to two parts
    middle = (a+b) / 2

    # b - a is a range of finding the root so it
    # indicates when middle could be a root, if of course b - a will be smaller than precision
    if b - a <= precision:
        return middle

    # in here and in return below the if statement, code determines whether root will be in one section or a second one
    # so the first if will be looking between left half and outside if will be looking between right half of a function
    if f(a) * f(middle) < 0:
        return roots(a, middle, precision)

    return roots(middle, b, precision)

print(roots(12, -2, 0.001))