class KataTest:
    def assert_equals(self, actual, expect, explain=""):
        print(explain, "\n", "actual:", actual, "\n", "expect:", expect)
        assert actual == expect
