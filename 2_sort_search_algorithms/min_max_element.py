# Naive algorithm for finding min and max position in a set
# Time complexity O(2n)
def min_max_find_naive_algo(lst):
    min_element = lst[0]
    max_element = lst[0]

    for element in lst:
        if element < min_element:
            min_element = element
    for element in lst:
        if element > max_element:
            max_element = element
    return min_element, max_element

# Optimal algorithm
# Time complexity: O(n)
def min_max_find_optimal_algo(lst):
    min_element = lst[0]
    max_element = lst[0]

    for element in lst:
        if element < min_element:
            min_element = element
        if element > max_element:
            max_element = element
    return min_element, max_element


print(min_max_find_naive_algo([1, 27, 21, 19, 88, 37, 1, -1]))
