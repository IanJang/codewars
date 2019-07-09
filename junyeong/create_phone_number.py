from junyeong import Test


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def test_create_phone_number():
    Test.describe("Basic tests")
    Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
    Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
    Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
    Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
    Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

    Test.assert_equals(create_phone_number([0, 1, 0, 1, 2, 3, 4, 5, 6, 7]), "(010) 123-4567")
