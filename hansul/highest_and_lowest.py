"""
http://www.codewars.com/kata/highest-and-lowest/train/python
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
"""
def high_and_low(numbers):
    int_numbers = list(map(int, numbers.split(" ")))
    high = sorted(int_numbers)[-1]
    low = sorted(int_numbers)[0]
    return "{} {}".format(high, low)


def test_highest_and_lowest():
    assert high_and_low("1 2 3 4 5") == "5 1"
    assert high_and_low("1 2 -3 4 5") == "5 -3"
    assert high_and_low("1 9 3 4 -5") == "9 -5"
    assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
