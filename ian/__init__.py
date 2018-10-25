class Test:
    @classmethod
    def assert_equals(cls, a, b, text):
        assert a == b
        print(text)

    @classmethod
    def it(cls, text):
        print(text)
