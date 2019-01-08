# https://www.codewars.com/kata/moving-zeros-to-the-end/train/python
from hansul import KataTest


def move_zeros(array):
    lst = []
    for n in array:
        if isinstance(n, bool) or n != 0:
            lst.append(n)
    lst.extend([0]*(len(array)-len(lst)))
    return lst


def test():
    Test = KataTest()
    Test.assert_equals(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    Test.assert_equals(
        move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Test.assert_equals(move_zeros(
        ["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Test.assert_equals(move_zeros(
        ["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]),
        ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Test.assert_equals(move_zeros([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0])
    Test.assert_equals(move_zeros(["a", "b"]), ["a", "b"])
    Test.assert_equals(move_zeros(["a"]), ["a"])
    Test.assert_equals(move_zeros([0, 0]), [0, 0])
    Test.assert_equals(move_zeros([0]), [0])
    Test.assert_equals(move_zeros([False]), [False])
    Test.assert_equals(move_zeros([]), [])
