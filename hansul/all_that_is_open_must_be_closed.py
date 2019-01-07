# https://www.codewars.com/kata/all-that-is-open-must-be-closed-dot-dot-dot/train/python
from hansul import KataTest

# def is_balanced(source, caps):
#     caps_map = {}
#     for i in range(0, len(caps), 2):
#         open_cap = caps[i]
#         close_cap = caps[i+1]
#         caps_map[open_cap] = close_cap
#
#     def is_open_cap(w):
#         return w in caps_map.keys()
#
#     def is_close_cap(w):
#         return w in caps_map.values()
#
#     stack = []
#     res = []
#     for w in source:
#         if is_open_cap(w) and is_close_cap(w):
#             t = "{}{}".format(w, w)
#             if t not in res:
#                 res.append(t)
#             if not stack:
#                 stack.append(w)
#             else:
#                 if stack[-1] == w:
#                     stack.pop()
#                 else:
#                     stack.append(w)
#             continue
#
#         if is_open_cap(w):
#             t = "{}{}".format(w, caps_map[w])
#             if t not in res:
#                 res.append(t)
#             stack.append(w)
#         elif is_close_cap(w):
#             if not stack:
#                 return False
#             if caps_map[stack[-1]] == w:
#                 stack.pop()
#             else:
#                 return False
#
#     if len(stack) != 0:
#         return False
#
#     return not res or "".join(res) == caps


def is_balanced(s, caps):
    stack = []
    openers, closers = caps[::2], caps[1::2]
    for char in s:
        if char in openers:
            if char in closers and stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        elif char in closers:
            if not stack or openers[closers.index(char)] != stack[-1]:
                return False
            else:
                stack.pop()
    return not stack


def test():
    test = KataTest()
    test.assert_equals(is_balanced("(Sensei says yes!)", "()"), True)
    test.assert_equals(is_balanced("(Sensei says no!", "()"), False)

    test.assert_equals(is_balanced("(Sensei [says] yes!)", "()[]"), True)
    test.assert_equals(is_balanced("(Sensei [says) no!]", "()[]"), False)

    test.assert_equals(is_balanced("Sensei says -yes-!", "--"), True)
    test.assert_equals(is_balanced("Sensei -says no!", "--"), False)
    test.assert_equals(is_balanced("(((Hello)))", "()"), True)
    test.assert_equals(is_balanced("(Hello Mother can you hear me?))", "()"), False)
    test.assert_equals(is_balanced("-a@b@cd@e@fghi-", "--@@"), True)
