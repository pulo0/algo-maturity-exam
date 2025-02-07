# Horner's Schema is pretty self-explanatory
# if you learned about polynomials and dividing them then you probably heard about Horner's Method
# the main premise of it in this case is to calculate the value of the polynomial based on x, so basically similar
# to schema on dividing but no we don't have any roots there, just calculating the value
# so, it's just doing a result * x + i until you scim through every number in set, and that's the result, easy
# use cases: changing bases, from binary to decimal, or quick exponentiation of a number
# Time complexity O(n)
def horner_method(num: list, x: int):
    result = 0
    for i in num:
        result = result * x + i
    return result

print(horner_method([1, 0, 1, 1, 0], 2))