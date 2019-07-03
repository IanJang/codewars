from junyeong import Test

def ordered_count(input):
    result = {}
    for c in input:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return list(result.items())

def test_ordered_count():
    test = Test()
    test.describe("Basic Tests")

    tests = (
        ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
        ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)]),
        ('Junyeong', [('J', 1), ('u', 1), ('n', 2), ('y', 1), ('e', 1), ('o', 1), ('g', 1)]),
        ('a1b2c3a4', [('a', 2), ('1', 1), ('b', 1), ('2', 1), ('c', 1), ('3', 1), ('4', 1)]),
        ('한글한글', [('한', 2), ('글', 2)]),
    )

    for t in tests:
        inp, exp = t
        test.assert_equals(ordered_count(inp), exp)
