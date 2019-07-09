from junyeong import Test


def valid_parentheses(string):
    check = 0
    for s in string:
        if s == '(':
            check += 1
        if s == ')':
            if check <= 0:
                return False
            check -= 1
    return check == 0


def test_valid_parentheses():
    Test.assert_equals(valid_parentheses("  ("), False)
    Test.assert_equals(valid_parentheses(")test"), False)
    Test.assert_equals(valid_parentheses(""), True)
    Test.assert_equals(valid_parentheses("hi())("), False)
    Test.assert_equals(valid_parentheses("hi(hi)()"), True)

    Test.assert_equals(valid_parentheses(")("), False)
    Test.assert_equals(valid_parentheses("if(valid_parentheses('()'))"), True)
    Test.assert_equals(valid_parentheses("public void run())"), False)


if __name__ == '__main__':
    print(valid_parentheses(")test"))
