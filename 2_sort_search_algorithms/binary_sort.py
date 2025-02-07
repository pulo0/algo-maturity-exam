# In this case you will need to know two algorithms to make binary sort
# - binary search and linear insertion sort
# also binary search can be made either recursively and iteratively
# but in my case, I use recursive approach because in my opinion is much more readable
# but either of paths you will go to, it'll be always O(log n)

# Time complexity: O(log n) for binary search
def binary_search(lst, desired_elem, left, right):
    # left and right are variables that indicate first and last index of the set
    # if the left (which for example in the beginning is always 0) is greater than right then return left
    # instead of returning -1 in normal binary search, because we want to sort using binary search
    if left > right: return left
    # calculation the middle of the set (meaning middle index)
    middle = (left+right) // 2
    # and now we go to main functionality of the binary search
    # three if statements:
    # first one is the easiest because if the calculated middle is the element we want to find
    # then there we go
    # second if, and corresponding to it else, determines whether binary search will continue on the left side or
    # the right side of the set (if is for left and else for right)
    # example: we have a set: [1, 2, 4, 5, 6, 7], we want to find 2 so binary search will do a middle then
    # (0+5)/2 = 2.5 = 2 (because // rounds down) and we have second if so 2 < 4 so binary search will go to the left side
    # meaning left = 0 and right = 2 - 1 = 1 then search will divide to the middle in 1 which is position where 2 lies
    if desired_elem == lst[middle]:
        return middle
    if desired_elem < lst[middle]:
        return binary_search(lst, desired_elem, left, middle - 1)
    else:
        return binary_search(lst, desired_elem, middle + 1, right)

# Time complexity: O(n log n) for binary sort (using binary search)
def binary_sort(lst):
    for i in range(1, len(lst)):
        main_element = lst[i]
        j = i - 1
        # main difference to insertion sort is this little line with position for binary search
        # j as right in parameters and 0 for left because left will always start at 0 and max of the set will be determined
        # by j just like previous version
        position = binary_search(lst, main_element, 0, j)
        while j >= position:
            lst[j+1] = lst[j]
            j = j - 1
        lst[position] = main_element
    return lst

n = list(map(int, input('Select your entries: ').split()))
print(binary_sort(n))