from junyeong import Test

def make_readable(seconds):
    sec = seconds % 60
    minute = seconds // 60 % 60
    hour = seconds // 60 // 60
    ret = "{:02d}:{:02d}:{:02d}".format(hour, minute, sec)
    return ret

def test_make_readable():
    Test.assert_equals(make_readable(0), "00:00:00")
    Test.assert_equals(make_readable(5), "00:00:05")
    Test.assert_equals(make_readable(60), "00:01:00")
    Test.assert_equals(make_readable(86399), "23:59:59")
    Test.assert_equals(make_readable(359999), "99:59:59")
