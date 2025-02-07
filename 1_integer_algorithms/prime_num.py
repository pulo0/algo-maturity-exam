import math as m


# Recursive approach with time complexity - O(n)
def check_if_prime(num: int, div: int = 2):
    if num % div != 0:
        check_if_prime(num, div.__add__(1))
    elif div == num:
        print('The number is a prime number')
    else:
        print('The number is not a prime number')


# More time efficient way, complexity: O(sqrt(n))
def is_prime(num: int):
    for i in (
    2, int(m.sqrt(num)) + 1):  # And this +1 is for the safety measure being range() func doesn't register the last item
        if (num % i) == 0:
            return False
    return True


check_if_prime(97)
print(is_prime(23))
