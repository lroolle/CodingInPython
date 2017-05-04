#!/usr/bin/env python3


import unittest
import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort1, insertion_sort2
from merge_sort import merge_sort
from quick_sort import qsort1, qsort2, qsort3, qsort4
from selection_sort import selection_sort
from shell_sort import shell_sort
from heap_sort import heap_sort


def is_sorted(a):
    return all(a[i] < a[i + 1] for i in range(len(a) - 1))


def create_unsorted(size, max_num=10000):
    return random.sample(range(max_num), size)


def create_sorted(size):
    return list(range(size))


class TestSorts(unittest.TestCase):
    def setUp(self):
        self.unsorted = create_unsorted(10000)
        self.sorted = create_sorted(10000)

    def test_bubble_sort(self):
        self.assertTrue(is_sorted(bubble_sort(create_unsorted(10000))))

    def test_bubble_sort_sorted(self):
        self.assertTrue(is_sorted(bubble_sort(self.sorted)))

    def test_insertion_sort1(self):
        self.assertTrue(is_sorted(insertion_sort1(create_unsorted(10000))))

    def test_insertion_sort1_sorted(self):
        self.assertTrue(is_sorted(insertion_sort1(self.sorted)))

    def test_insertion_sort2(self):
        self.assertTrue(is_sorted(insertion_sort2(create_unsorted(10000))))

    def test_insertion_sort2_sorted(self):
        self.assertTrue(is_sorted(insertion_sort2(self.sorted)))

    def test_selection_sort(self):
        self.assertTrue(is_sorted(selection_sort(create_unsorted(10000))))

    def test_selection_sort_sorted(self):
        self.assertTrue(is_sorted(selection_sort(self.sorted)))

    def test_shell_sort(self):
        self.assertTrue(is_sorted(shell_sort(create_unsorted(10000))))

    def test_shell_sort_sorted(self):
        self.assertTrue(is_sorted(shell_sort(self.sorted)))

    def test_merge_sort(self):
        self.assertTrue(is_sorted(merge_sort(create_unsorted(10000))))

    def test_merge_sort_sorted(self):
        self.assertTrue(is_sorted(merge_sort(self.sorted)))

    def test_qsort1(self):
        self.assertTrue(is_sorted(qsort1(create_unsorted(10000))))

    def test_qsort1_sorted(self):
        self.assertTrue(is_sorted(qsort1(self.sorted)))
        # failed
        # RecursionError: maximum recursion depth exceeded in comparison

    def test_qsort2(self):
        self.assertTrue(is_sorted(list(qsort2(create_unsorted(10000)))))

    def test_qsort2_sorted(self):
        self.assertTrue(is_sorted(list(qsort2(create_sorted(10000)))))

    def test_qsort3(self):
        # qsort3 is in-place sort
        a = create_unsorted(10000)
        self.assertFalse(is_sorted(a))
        qsort3(a, 0, len(a) - 1)
        self.assertTrue(is_sorted(a))

    def test_qsort4(self):
        # in-place sort
        a = create_unsorted(10000)
        self.assertFalse(is_sorted(a))
        qsort4(a, 0, len(a) - 1)
        self.assertTrue(is_sorted(a))

    def test_heap_sort(self):
        self.assertTrue(is_sorted(heap_sort(create_unsorted(10000))))

    def test_heap_sort_sorted(self):
        self.assertTrue(is_sorted(heap_sort(create_sorted(10000))))


if __name__ == '__main__':
    unittest.main()
