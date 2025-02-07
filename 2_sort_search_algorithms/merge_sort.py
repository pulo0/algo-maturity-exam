import random
test_arr = [random.randint(1, 10000) for _ in range(random.randint(100, 10000))]

# In this script let's examine how merge sort works
# (of course in my words, I hope I'll convey it as precise as possibly can)
# so let's go

# Merge sort in my at least version (also found in polish textbooks or sites like ZPE)
# also in here: https://www.geeksforgeeks.org/merge-sort/#how-does-merge-sort-work,
# it consists of two methods, one is for proper sorting and one is for merging arrays
# but overall it uses recursion to loop itself to slip into smaller parts of the array and then sort itself from
# smaller pieces to a whole
def merge(arr, left, right, mid):
    # n1 and n2 indicate how many elements are in left and right half of the set (n1 for left, n2 for right)
    # example: let's get a set of 6 elements (5 is the max index)
    # dividing it to middle would be (0+5) // 2 = 2 and then going straight to n1 = 2 - 0 + 1 = 3, and there is actually
    # that amount of numbers in set on the left side
    # n2 = 5 - 2 = 3, also exact same number because there are 6 elements and 6/2=3, on each side there are 3 elements each
    n1 = mid - left + 1
    n2 = right - mid

    # L = left temp array and R = right temp array
    # here we assign how big will be each array (for now it'll be: L = [0, 0, 0] and R = [0, 0, 0])
    L = [0] * n1
    R = [0] * n2

    # and here we have two for loops to assign to L and R arrays each element from their corresponding side
    # mid + 1 + j will be like 2 + 1 + j (j will equal to max 3, range 0 to 3)
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    # i and j are indexing for left and right array respectively
    # k is for main array to go through is from beginning to end
    i = 0
    j = 0
    k = left

    # main part of the algorithm
    # in here we decide whether elements in L and R elements are greater from each other
    # if one side the less than the other, then the smaller side will go first to the array and then index will go up
    # because we don't want to count this element anymore, and the 'overall' index also goes up because we found the
    # adequate element
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i + 1
        else:
            arr[k] = R[j]
            j = j + 1
        k = k + 1

    # in here, if after the first loop there's still left in the array L and index i didn't match to n1
    # (like it's still 2 and n1 = 4 for example)
    # and assigns right away, indexes go up too
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # same as above but now on the right side, R
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Time complexity: O(n log n)
def merge_sort(arr, left, right):
    # main logic of sorting
    # it uses recursion to make left side and right side of the array
    # and then merge it at the end
    # also in second merge_sort (right side) middle + 1 would be 2 + 1 = 3 so appropriate size of the right size
    # (from index 3 to index 5, 3,4,5)
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, right, middle)

# n = list(map(int, input('Select your entries: ').split()))
merge_sort(test_arr, 0, len(test_arr) - 1)
print(test_arr)