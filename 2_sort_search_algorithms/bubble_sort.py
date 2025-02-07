# Time complexity: O(n^2)
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(bubble_sort([2, 31, 1, 21, 42, 5213, 321, 32, 42]))