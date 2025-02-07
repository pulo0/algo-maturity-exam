# Time complexity: O(sqrt(n))
def factory_num(num: int):
    factor = 2  # the smallest prime number (2 because 2 and 1 are only the numbers that can be divided by 2)
    while factor * factor <= num:
        while num % factor == 0:
            print(f'{factor}\t', end='')
            num = num // factor
        factor += 1
    if num > 1:
        print(f'{num}\t')


factory_num(4)