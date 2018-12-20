# 4kyu
# https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python
import operator

from hansul import KataTest

def solve_runes(runes):
    class PlaceHolder:
        def __init__(self):
            self.value = None

    operater_map = {
        "-": operator.sub,
        "+": operator.add,
        "*": operator.mul,
    }

    converted_slots = []
    placeholder = PlaceHolder()

    # 숫자, 연산자 파싱
    for rune in runes:
        if rune.isdigit():
            converted_slots.append(int(rune))
        else:
            if rune in operater_map.keys():
                converted_slots.append(operater_map[rune])
            elif rune == "?":
                converted_slots.append(placeholder)
            else:
                continue
    #
    # # 2차 convert
    # result_value = None
    # computed_value = None
    # converted_slots_2 = []
    # v = 1
    #
    # for slot in converted_slots:
    #
    #     if type(slot) is int:
    #         # 숫자, 숫자인경우
    #         if type(computed_value) is int:
    #             v = v * 10
    #             computed_value = computed_value * v
    #             computed_value += slot
    #         # 연산자, 숫자인경우
    #
    #     elif slot is not placeholder:
    #         v = 1
    #
    #
    #
    #     if result_value is None:
    #         result_value = computed_value





def test_find_the_unknown_digit():
    test = KataTest()
    test.assert_equals(solve_runes("1+1=?"), 2, "Answer for expression '1+1=?' ");
    test.assert_equals(solve_runes("123*45?=5?088"), 6, "Answer for expression '123*45?=5?088' ");
    test.assert_equals(solve_runes("-5?*-1=5?"), 0, "Answer for expression '-5?*-1=5?' ");
    test.assert_equals(solve_runes("19--45=5?"), -1, "Answer for expression '19--45=5?' ");
    test.assert_equals(solve_runes("??*??=302?"), 5, "Answer for expression '??*??=302?' ");
    test.assert_equals(solve_runes("?*11=??"), 2, "Answer for expression '?*11=??' ");
    test.assert_equals(solve_runes("??*1=??"), 2, "Answer for expression '?*11=??' ");