import unittest
import random
from recursive_sorting import *
from basic_recursion import *


class RecursiveSortingTests(unittest.TestCase):
    def test_merge_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [2]
        arr4 = [0, 1, 2, 3, 4, 5]
        arr5 = random.sample(range(200), 50)

        self.assertEqual(merge_sort(arr1), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(merge_sort(arr2), [])
        self.assertEqual(merge_sort(arr3), [2])
        self.assertEqual(merge_sort(arr4), [0, 1, 2, 3, 4, 5])
        self.assertEqual(merge_sort(arr5), sorted(arr5))

    # Uncomment this test to test your in-place merge sort implementation
    # def test_in_place_merge_sort(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [2]
    #     arr4 = [0, 1, 2, 3, 4, 5]
    #     arr5 = random.sample(range(200), 50)

    #     self.assertEqual(merge_sort_in_place(arr1, 0, len(arr1)-1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(merge_sort_in_place(arr2, 0, len(arr2)-1), [])
    #     self.assertEqual(merge_sort_in_place(arr3, 0, len(arr3)-1), [2])
    #     self.assertEqual(merge_sort_in_place(arr4, 0, len(arr4)-1), [0,1,2,3,4,5])
    #     self.assertEqual(merge_sort_in_place(arr5, 0, len(arr5)-1), sorted(arr5))

    def test_merge_sort2(self):
        test_arr = [5, 1, 3]
        test_arr_2 = [10, 8, 75, 31, 3]
        assert merge_sort(test_arr) == [1, 3, 5]
        assert merge_sort(test_arr_2) == sorted(test_arr_2)

    def test_facto(self):
        assert facto(3) == 6

    def test_recursive_linear(self):
        assert recursive_linear(random.sample(range(10), 10), 7) == True
        assert recursive_linear(random.sample(range(10), 10), 15) == False

    def test_recursive_linear_alt(self):
        assert recursive_linear_alt(random.sample(range(10), 10), 7) == True
        assert recursive_linear_alt(random.sample(range(10), 10), 15) == False


if __name__ == '__main__':
    unittest.main()
