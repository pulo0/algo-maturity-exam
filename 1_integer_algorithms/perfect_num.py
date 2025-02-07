# Time complexity: O(n)
def is_perfect(num: int):
    result = 1
    for i in range(2, num//2+1):
        if num % i == 0:
            result += i
    return result == num

print(is_perfect(28))