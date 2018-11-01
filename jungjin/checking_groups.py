"""
https://www.codewars.com/kata/checking-groups/train/python
In English and programming, groups can be made using symbols such as () and {} that change meaning. However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping. For instance, the following groups are done correctly:

({})
[[]()]
[{()}]
The next are done incorrectly:

{(})
([]
[])
A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.

Your function will take an input string that may contain any of the symbols (), {} or [] to create groups.

It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.
"""


# By.고운 대리님
# c_set = {'(': ')', '[': ']', '{': '}', ')': '#', ']': '#', '}': '#'}
# def group_check(s):
#     l = []
#     for c in list(s):
#         if len(l) == 0:
#             l.append(c)
#         else:
#             if c_set[l[-1]] == c:
#                 l.pop(-1)
#             else:
#                 l.append(c)
#
#     if len(l) > 0:
#         return False
#     else:
#         return True

def next_string(v):
    if v == "(":
        return ")"
    if v == "{":
        return "}"
    if v == "[":
        return "]"


def group_check(s):
    if len(s) == 0:
        return True
    if (s.count('(') + s.count(')')) % 2 == 1:
        return False
    if (s.count('{') + s.count('}')) % 2 == 1:
        return False
    if (s.count('[') + s.count(']')) % 2 == 1:
        return False
    if (len(s) % 2) == 1:
        return False
    for i in range(0, len(s)):
        s = s.replace('()', "")
        s = s.replace('{}', "")
        s = s.replace('[]', "")
        if len(s) == 0:
            return True
    return False


def test_highest_and_lowest():
    assert group_check("()") is True
    assert group_check("({") is False
    assert group_check("({})") is True
    assert group_check("[[]()]") is True
    assert group_check("[{()}]") is True
    assert group_check("{(})") is False
    assert group_check("([]") is False
    assert group_check("[])") is False
