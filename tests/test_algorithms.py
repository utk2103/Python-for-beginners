"""Tests for the search and sort scripts.

Run from the repo root:
    python -m unittest discover tests
"""

import contextlib
import importlib.util
import io
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"


def load(filename):
    # Why: names like "01.TwoSum.py" can't be imported with `from scripts.x import y`
    spec = importlib.util.spec_from_file_location(filename, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):  # Why: some scripts print at import
        spec.loader.exec_module(module)
    return module


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.search = load("BinarySearch.py").binarySearch

    def find(self, array, x):
        return self.search(array, x, 0, len(array) - 1)

    def test_finds_element(self):
        array = [3, 4, 5, 6, 7, 8, 9]
        for i, value in enumerate(array):
            self.assertEqual(self.find(array, value), i)

    def test_missing_element(self):
        self.assertEqual(self.find([3, 4, 5], 99), -1)

    def test_empty_array(self):
        self.assertEqual(self.find([], 1), -1)


class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.search = load("LinearSearch.py").linearSearch

    def test_finds_element(self):
        array = [2, 4, 0, 1, 9]
        self.assertEqual(self.search(array, len(array), 1), 3)

    def test_returns_first_match(self):
        array = [7, 7, 7]
        self.assertEqual(self.search(array, len(array), 7), 0)

    def test_missing_element(self):
        self.assertEqual(self.search([2, 4], 2, 5), -1)


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.sort = load("MergeSort.py").mergeSort

    def sorted_copy(self, array):
        array = list(array)
        self.sort(array)  # Why: sorts in place, returns None
        return array

    def test_sorts_in_place(self):
        self.assertEqual(self.sorted_copy([6, 5, 12, 10, 9, 1]), [1, 5, 6, 9, 10, 12])

    def test_duplicates_and_negatives(self):
        self.assertEqual(self.sorted_copy([3, -1, 3, 0, -1]), [-1, -1, 0, 3, 3])

    def test_short_inputs(self):
        self.assertEqual(self.sorted_copy([]), [])
        self.assertEqual(self.sorted_copy([42]), [42])
        self.assertEqual(self.sorted_copy([2, 1]), [1, 2])


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solve = load("01.TwoSum.py").Solution().twoSum

    def test_returns_indices_of_pair(self):
        nums, target = [2, 7, 11, 15], 9
        i, j = self.solve(nums, target)
        self.assertNotEqual(i, j)
        self.assertEqual(nums[i] + nums[j], target)

    def test_unsorted_input(self):
        nums, target = [3, 2, 4], 6
        i, j = self.solve(nums, target)
        self.assertEqual(sorted([nums[i], nums[j]]), [2, 4])

    def test_no_pair_returns_empty_list(self):
        self.assertEqual(self.solve([1, 2, 3], 100), [])


if __name__ == "__main__":
    unittest.main()
