# Time complexity: O(n^2)
def selection_sort(lst):
    for i in range(len(lst)):
        main_index = i # sets the first index that will be compared to in the inner loop
        # for example let's say we have this set of nums: [4, 2, 1, 4, 5, 6, 7]
        # so the main_index will hook onto in first iteration number 4
        # then it goes through all numbers in search of the biggest than 4
        # (that's why i+1 at start because we don't want to redundantly compare the first number)
        for j in range(i+1, len(lst)):
            # in here we have comparing phase of the algorithm
            # and if the main number is greater than searched number then swap the index to it,
            # it will switch the indexes until it finds the biggest value
            if lst[main_index] > lst[j]:
                main_index = j
        # then out of inner loop the 'i' indicates now the main number
        # and main_index is the desired number to switch to the end of the set
        lst[main_index], lst[i] = lst[i], lst[main_index]
    return lst

print(selection_sort([2, 31, 1, 21, 42, 5213, 321, 32, 42]))