import math
from junyeong import Test


# def zeros(n):
#    ret = math.ceil(n / 5) + 1
#    return ret


def zeros2(n):
    rev_str = str(math.factorial(n))[::-1]
    count = 0
    for c in rev_str:
        # print(n)
        if c != '0':
            break
        count += 1
    return count


def zeros(n):
    ret = 0
    i = 5
    while i < n:
        ret += n // i
        i *= 5
    return ret


def test_all():
    test = Test()
    test.describe("Sample Tests")
    test.it("Should pass sample tests")

    test.assert_equals(zeros(0), 0, "Testing with n = 0")
    test.assert_equals(zeros(6), 1, "Testing with n = 6")
    test.assert_equals(zeros(30), 7, "Testing with n = 30")
