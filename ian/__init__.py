class Test:
    @classmethod
    def assert_equals(cls, a, b, text=None):
        assert a == b
        print(text)

    @classmethod
    def it(cls, text):
        print(text)


class KataTest(Test):
    pass
