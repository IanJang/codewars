import re


class Calculator(object):
    def evaluate(self, string):
        # 숫자와 연산자가 아니면 모두 제거
        string = re.sub('[^0-9^*/+-^\\s]', '', string)
        splitted = string.split()
        i = 0
        while i < len(splitted) - 1:
            c = splitted[i]
            if c == '*' or c == '/':
                splitted[i] = self.calculate(splitted[i - 1], splitted[i + 1], c)
                del splitted[i + 1]
                del splitted[i - 1]
                i -= 2
            i += 1
        i = 0
        while i < len(splitted) - 1:
            c = splitted[i]
            if c == '+' or c == '-':
                splitted[i] = self.calculate(splitted[i - 1], splitted[i + 1], c)
                del splitted[i + 1]
                del splitted[i - 1]
                i -= 2
            i += 1
        return float(splitted[0])

    def calculate(self, x, y, operator):
        x = float(x)
        y = float(y)
        if operator == '*':
            return x * y
        elif operator == '/':
            return x / y
        elif operator == '+':
            return x + y
        elif operator == '-':
            return x - y


calc = Calculator()
calc.evaluate("2 / 2 + 3 * 4 - 6")


def test_calculator():
    calc = Calculator()

    assert calc.evaluate("2 / 2 + 3 * 4 - 6") == 7
    assert calc.evaluate("3 * 4 + 2 / 2 - 6") == 7
    assert calc.evaluate("1 + 2 * 3") == 7
