import bisect
import collections
import queue

# queue
q = queue.SimpleQueue()

# Counter. return a dict
cnt = collections.Counter([1, 2, 3, 4, 3, 33, 2, 2, 3, 3, 2, 2, 2, 2])

# binary search
# bisect_left return the leftmost index
index = bisect.bisect_left([1, 2, 3, 3, 4, 5], 3)
# insert the item in the leftmost position of arr.
bisect.insort_left([1, 2, 3, 4, 5, 6, 6, 7], 6)
