# 4kyu
# https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python
from hansul import KataTest


def solve_runes(runes):
    rune_digits = set([int(rune) for rune in runes if rune.isdigit()])
    target_numbers = [i for i in range(0, 10) if i not in rune_digits]
    for i in target_numbers:
        replaced_runes = runes.replace("?", str(i))
        replaced_runes = replaced_runes.replace("=", "==")
        if replaced_runes.split("==")[-1].startswith("00"):
            continue
        try:
            if eval(replaced_runes) is True:
                return i
        except SyntaxError:
            continue
    return -1


def test_find_the_unknown_digit():
    test = KataTest()
    test.assert_equals(solve_runes("1+1=?"), 2, "Answer for expression '1+1=?' ")
    test.assert_equals(solve_runes("123*45?=5?088"), 6, "Answer for expression '123*45?=5?088' ")
    test.assert_equals(solve_runes("-5?*-1=5?"), 0, "Answer for expression '-5?*-1=5?' ")
    test.assert_equals(solve_runes("19--45=5?"), -1, "Answer for expression '19--45=5?' ")
    test.assert_equals(solve_runes("??*??=302?"), 5, "Answer for expression '??*??=302?' ")
    test.assert_equals(solve_runes("?*11=??"), 2, "Answer for expression '?*11=??' ")
    test.assert_equals(solve_runes("??*1=??"), 2, "Answer for expression '?*11=??' ")
    test.assert_equals(solve_runes("-491-34295=-34?86"), 7)
    test.assert_equals(solve_runes("-56*-17575=984?00"), 2)
    test.assert_equals(solve_runes("8264+-?9644=-?1380"), 5)
