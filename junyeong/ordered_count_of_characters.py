from junyeong import Test

def ordered_count(input):
    pass

def test_ordered_count():
    test = Test()
    test.describe("Basic Tests")

    tests = (
        ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
        ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
    )

    for t in tests:
        inp, exp = t
        test.assert_equals(ordered_count(inp), exp)