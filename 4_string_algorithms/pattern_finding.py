# This is a naive way of finding a pattern in a string
# complexity may vary, best case is linear and worst could be O(n*m)
# Time complexity: O(n)
def pattern_find(main: str, pattern: str) -> int:
    # first things first we create a for loop to iterate n times to find a matching pattern
    # why minus length of a pattern you may ask? Well, because we iterate in while loop through j times
    # and knowing that j can be maximum of pattern length because this way we are finding a pattern
    # then we wouldn't want to go out of bound (out of index), + 1 is to create an offset so that for loop could
    # even reach the pattern
    for i in range(len(main) - len(pattern) + 1):
        j = 0
        # while loop is here to 'catch' the pattern
        # it iterates until j will not surpass length of a pattern string
        # and second condition - letters of a pattern will even match to main string,
        # and then it'll go through the pattern because if at least one letter will be found then it'll until
        # it finished the pattern, or also it will not be the pattern and will go to the next iteration, this time in
        # for loop
        while j < len(pattern) and pattern[j] == main[i + j]:
            j += 1

        # and here at the end, if j will be the same length to a pattern then congratulation
        # you have found your pattern
        if j == len(pattern):
            return i
    return -1

print(f'Index of pattern is at: {pattern_find('I have a cat', 'cat')}')