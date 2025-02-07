import math as m

# Pretty slow, but it can be made iterative with linear complexity
# Time complexity: O(2^n)
def fibonacci_seq_recursive(seq_len: int):
    if seq_len <= 2:
        return 1
    return fibonacci_seq_recursive(seq_len-2) + fibonacci_seq_recursive(seq_len-1)

# Time complexity: O(n)
def fibonacci_seq_iterative(seq_len: int):
    a, b = 1, 1
    for i in range(seq_len-1):
        b += a
        a = b - a
    return a

# Extra: Binet's Formula is the most effective to find nth fibonacci number
# Time complexity: O(1)
def binet_formula(nth_fib: int):
    phi = (m.sqrt(5)+1) / 2
    psi = (m.sqrt(5)-1) / 2
    return round((pow(phi, nth_fib) - pow(psi, nth_fib)) / m.sqrt(5))

n = int(input('Enter number of sequences: '))

print(fibonacci_seq_recursive(n))
print(fibonacci_seq_iterative(n))
print(binet_formula(n))