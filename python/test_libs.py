import bisect
import collections
import heapq
import queue
import unittest


class TestLibs(unittest.TestCase):
    def test_queue(self):
        q = queue.SimpleQueue()
        q.put(1)
        self.assertEqual(q.get(), 1)

    def test_counter(self):
        # Counter. return a dict
        counter = collections.Counter([1, 2, 3, 4, 3, 33, 2, 2, 3, 3, 2, 2, 2, 2])

    def test_bisect(self):
        # binary search
        # bisect_left return the leftmost index
        index = bisect.bisect_left([1, 2, 3, 3, 4, 5], 3)
        # insert the item in the leftmost position of arr.
        bisect.insort_left([1, 2, 3, 4, 5, 6, 6, 7], 6)

    def test_heap(self):
        h = []
        heapq.heapify(h)
        heapq.heappush(h, [0, 1])
