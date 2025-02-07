# Insertion sort in the set is similar to a sorting cards in for example - poker
# Time complexity: O(n^2) (best case - O(n))
def linear_sort(lst):
    # firstly the main loop is for aligning the main number that you will compare other to
    # and the main number will be in second position in the set (which is 1 because set indexing starts at 0)
    # and then you will compare backwards, to the previous positions
    for i in range(1, len(lst)):
        # inserted_element is for setting the main number you will compare other numbers if it's smaller than those
        inserted_element = lst[i]
        # j is an index (because while loop doesn't create indexes like for loops) and it sets the previous position
        j = i - 1
        # and now inner loop, it checks first - if j is greater or equal to 0 to not go out of range, or rather backwards
        # second parameter is important
        # if the previous position is greater than our selected then:
        while j >= 0 and lst[j] > inserted_element:
            # it 'duplicates' the previous position value to a further position and lowers j index
            # in order to mitigate then range of comparing values in set
            # also it does it until the j will be 0 (included) because this will be the end of the set
            lst[j + 1] = lst[j]
            j = j - 1
        # then at the end it inserts saves above the main number in set to put it in place where is a duplicate
        # for example after sorting it would look like [1, 3, 3, 4] so inserted_element = 2,
        # it'll be like this [1, 2, 3, 4]
        lst[j + 1] = inserted_element
    return lst

n = list(map(int, input('Select your entries: ').split()))
print(linear_sort(n))
