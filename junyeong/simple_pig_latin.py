from junyeong import Test
import string

def pig_it(text):
    # 1.나눈다
    # 2.첫 번째 문자와 나머지를 분리한다
    # 3. 각 문자열 맨 뒤에 ay를 붙인다 (punctuation marks에는 ay를 붙이지 않는다)

    splitted = text.split()
    ret = []
    for s in splitted:
        head = s[0]
        body = s[1:]
        result = body + head
        if head not in string.punctuation:
            result = body + head + 'ay'
        ret.append(result)
    return ' '.join(ret)

def test_pig_ig():
    Test.assert_equals(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
    Test.assert_equals(pig_it('This is my string'), 'hisTay siay ymay tringsay')
    Test.assert_equals(pig_it('Python and django'), 'ythonPay ndaay jangoday')
    Test.assert_equals(pig_it('My name is Junyeong !'), 'yMay amenay siay unyeongJay !ay')

if __name__ == '__main__':
    pig_it('O tempora o mores !')