from junyeong import Test, Test1
import string


def mix(s1, s2):
    cnt = {}
    for c in string.ascii_lowercase:
        cnt1 = s1.count(c)
        cnt2 = s2.count(c)
        if not (cnt1 is 0 and cnt2 is 0):
            sub = abs(cnt1 - cnt2)
            max_one = max(cnt1, cnt2)
            which_max = 1 if max_one == cnt1 else 2
            if max_one > 1:
                cnt[c] = (max_one, sub, which_max)
    ret = []
    for c in cnt:
        head = '=' if cnt[c][1] is 0 else str(cnt[c][2])
        ret.append(head + ":" + c * cnt[c][0])

    dic = {dpo(s): s for s in ret}
    sorted_keys = sorted(dic, reverse=True)
    sorted_values = [dic[k] for k in sorted_keys]
    return '/'.join(sorted_values)


def dpo(element):
    _dpo = 0

    chars = element[2:]
    count = len(chars)

    _dpo += count * 10000000
    op = element[:2]
    if op == '=:':
        pass
    elif op == '1:':
        _dpo += 2 * 10000
    elif op == '2:':
        _dpo += 1 * 10000

    rev_asc = ord('z') - ord(chars[0])
    _dpo += rev_asc
    return _dpo


def test_dpo():
    assert dpo('2:ee') > dpo('=:ee')
    assert dpo('1:ee') > dpo('2:ee')

    assert dpo('2:e') > dpo('2:f')
    assert dpo('2:ff') > dpo('2:e')

    assert dpo('2:ee') > dpo('2:ff')
    assert dpo('2:fff') > dpo('2:ee')

    assert dpo('1:ooo') > dpo('1:uuu')
    assert dpo('1:uuu') > dpo('2:sss')
    assert dpo('2:sss') > dpo('=:nnn')
    assert dpo('=:nnn') > dpo('1:ii')
    assert dpo('1:ii') > dpo('2:aa')
    assert dpo('2:aa') > dpo('2:dd')
    assert dpo('2:dd') > dpo('2:ee')
    assert dpo('2:ee') > dpo('2:gg')


def test_mix():
    Test.describe("Mix")
    Test.it("Basic Tests")
    Test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
    Test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"),
                       "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
    Test.assert_equals(mix(" In many languages", " there's a pair of functions"),
                       "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
    Test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
    Test.assert_equals(mix("codewars", "codewars"), "")
    Test.assert_equals(mix("A generation must confront the looming ", "codewarrs"),
                       "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")


if __name__ == '__main__':
    Test1.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
    Test1.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"),
                       "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
    Test1.assert_equals(mix(" In many languages", " there's a pair of functions"),
                       "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
    Test1.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
    Test1.assert_equals(mix("codewars", "codewars"), "")
    Test1.assert_equals(mix("A generation must confront the looming ", "codewarrs"),
                       "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")