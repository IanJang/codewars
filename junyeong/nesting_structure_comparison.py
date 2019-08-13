from junyeong import Test
import re


def same_structure_as(original, other):
    regex = '[\\[\\]\\,]'
    result1 = re.findall(regex, str(original).replace("'['", '').replace("']'", ''))
    result2 = re.findall(regex, str(other).replace("'['", '').replace("']'", ''))
    return str(result1) == str(result2)


def explore_structure(original):
    return str(original)


def test_all():
    Test.assert_equals(same_structure_as([1, [1, 1]], [2, [2, 2]]), True, "[1,[1,1]] same as [2,[2,2]]")
    Test.assert_equals(same_structure_as([1, [1, 1]], [[2, 2], 2]), False, "[1,[1,1]] not same as [[2,2],2]")


if __name__ == '__main__':
    print(same_structure_as([1, [1, 1]], [2, [2, 2]]))
    print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
    print(same_structure_as([1, '[', ']'], ['[', ']', 1]))
