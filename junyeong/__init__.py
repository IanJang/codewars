class Test:
    @classmethod
    def assert_equals(cls, a, b, text=None):
        assert a == b
        print(text)

    @classmethod
    def it(cls, text):
        print(text)

    expect = assert_equals

    @classmethod
    def describe(cls, text):
        print(text)


class KataTest(Test):
    pass

class Test1:
    @classmethod
    def assert_equals(cls, a, b, text=None):
        print({a == b: (a, b, len(a), len(b))})