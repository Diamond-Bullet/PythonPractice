import bisect
import collections
import heapq
import logging
import queue
import unittest
import decimal


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
        logging.info("#IMP# heap: ", h)

    def test_open_file(self):
        # r: read, w: write, a: append, b: open in binary format,
        file = open("/root/test", 'a')
        file1 = open("/root/test", 'wb')

    def test_decimal(self):
        # Decimal
        d1 = decimal.Decimal('0.1')
        d2 = decimal.Decimal('0.2')
        d3 = d1 + d2
        print(d3)
