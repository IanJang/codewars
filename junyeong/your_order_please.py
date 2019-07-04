from junyeong import Test
import re

def order(sentence):
    strs = sentence.split()
    li = list(dict(sorted({s: int(re.findall("\\d+", s)[0]) for s in strs}.items(), key=lambda kv: kv[1])).keys())
    return ' '.join(li)

def test_order():
    Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
    Test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
    Test.assert_equals(order(""), "")
    Test.assert_equals(order("junye5ong m1y c4hoi nam2e 3is"), "m1y nam2e 3is c4hoi junye5ong")


if __name__ == '__main__':
    order("Thi1s is2 3a T4est")