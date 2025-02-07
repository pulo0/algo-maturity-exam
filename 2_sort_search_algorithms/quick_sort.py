import random
test_arr = [random.randint(1, 10000) for _ in range(random.randint(100, 10000))]

# This is the 'in-place' version of quick sort
# Versions of Quick Sort are many, so there is a lot of room to play around, but it could be easily implemented badly
# but overall in-place version characteristics are that it doesn't use additional memory for new sets, but only using a
# courtesy of mutability of arrays
# Time complexity: O(n log n)
def quick_sort(arr, left, right):
    # first of, let's create variables that will be useful in the entire algorithm
    # i and j are respectively indexes for left and right side of the set
    # pivot is on the other hand a middle point that i and j will go towards and then also overlap
    # comparing each other (but firstly comparing to a pivot)
    i, j = left, right
    pivot = arr[(i+j)//2]

    # also a side note, pivot indicates the point in the array for two sides, left and right of course
    # but respective side needs to abide by their own rules:
    # left side (i) needs to be less than or equal to a pivot
    # right side (j) needs to be greater than or equal to a pivot
    # and by those rules they'll be switching places if left side will have a greater than pivot element and right will
    # have mirror opposite of course as an example

    # while True is used here to iterate the comparison between a pivot and those two sides until they will be both sorted
    # as much as they can because if it'll be something missing then recursion of the method will do its job
    while True:
        # those two while loops will run until the left side will have an element greater than pivot
        # and right side the opposite of course
        # also i += 1 so left index is going up because it's at the beginning
        # and j -= 1 is the right side so logically it will go towards left side
        while pivot > arr[i]:
            i += 1
        while pivot < arr[j]:
            j -= 1

        # if loop and its condition only indicate for the indexes to not go on each other grounds, side
        # i > j means that the array is sorted correctly, so else condition in this code
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            break

    # in here we sort out 'locally' each side for it to be sorted as well
    # first if is for left side (from [0 to j] index)
    # second if is for right side (from [i to len(arr)-1] index)
    if j > left:
        quick_sort(arr, left, j)

    if i < right:
        quick_sort(arr, i, right)

print(test_arr)
quick_sort(test_arr, 0, len(test_arr) - 1)
print(test_arr)