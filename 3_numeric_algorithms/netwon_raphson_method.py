# Of course, we don't need to use this algorithm if we have for example a library math with sqrt function
# but what if you will be prohibited from using sqrt? Well then you will need this method made by
# Newton Raphson
# Time complexity: O(log n)
def ar_root(n):
    # firstly we want to create a square with a,b side but for now we have a rectangular
    # with a shorter side - a with 1 and b, longer side with user picked number what you want to use a square root of
    # precision is of course pretty self-explanatory, to how much precision you want to see the square root
    a = 1
    b = n
    precision = .001
    while abs(a - b) >= precision:
        # in here we're making for a side 'a' an average of both sides and for b
        # just dividing it in half
        # and until a*b will not equal n then it'll iterate for this amount of time
        a = (a+b)/2
        b = n/a
    return (a+b)/2

print(ar_root(3))