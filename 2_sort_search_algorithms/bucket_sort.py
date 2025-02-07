import random
test_index = random.randint(10000, 100000)
test_arr = [random.randint(1, 10000) for _ in range(test_index)]

# In contrast to other algorithms, bucket sort requires you to know two additional parameters not counting the set:
# 1. size of the bucket or rather amount of buckets you want to create
# 2. max_range which is in my code max element number in set (like in [1, 2, 4, 5] set max will be 5)
# Time complexity: O(n)
def bucket_sort(arr: list, size: int, max_range: int):
    # p is for counting the ranges in certain buckets (like for example p = 20 so first bucket [index = 0] will have a range)
    # 0 ... to 20 and elements with numbers between 0 and 20 can go to bucket index 0
    p = max_range // size
    # creating 'size' amount of buckets, by this I mean arrays, nested arrays
    buckets = [[] for _ in range(size)]

    # the main 'elements are getting assigned to each buckets'
    # also the min is utilized for out of bound error, regarding index
    # because let's assume that we want to sort it in 5 buckets (from 0 to 4 buckets because indexing)
    # and p equals to 20 and there is an element 100 so the division will be 5, and yes, there are five buckets
    # but indexing messes this up because it starts from 0 so we need to you size - 1 to assign it the highest bucket
    for i in arr:
        buckets[min(size - 1, i // p)].append(i)

    # sort through all the buckets
    # if statement with > 1 we use because if there is only one item i the bucket then it's pretty pointless to sort it
    # you could, but it's just meaningless
    # sort() method uses Quick Sort to sort through the buckets so we utilize bucket method and are sort algorithms
    # 'bucket sort' is kinda only a method to get to sorting, it doesn't sort itself, a bit like binary sort
    # it itself doesn't sort but rather outsource it to insertion sort in addition to modified binary search to
    # make it more efficient than simple linear one
    for i in range(len(buckets)):
        if len(buckets[i]) > 1:
            buckets[i].sort()

    # adding already sorted buckets content to its own array to be concise
    # and returns it
    s_arr = []
    for bucket in buckets:
        s_arr.extend(bucket)

    return s_arr


print(bucket_sort(test_arr, 100, 10000))
