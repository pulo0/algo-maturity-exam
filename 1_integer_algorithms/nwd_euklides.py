# Time complexity: O(log n)
def nwd_euclides_recursive(a:int, b:int):
    if b > 0:
        return nwd_euclides_recursive(b, a%b)
    return a

# Also time complexity: O(log n)
def nwd_euclides_iterative(a:int, b:int):
    while b > 0:
        temp = a
        a = b
        b = temp%b
    return a

print(f'Recursive: {nwd_euclides_recursive(24, 28)}')
print(f'Iterative: {nwd_euclides_iterative(24, 1000)}')