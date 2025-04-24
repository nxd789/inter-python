def parse(s):
    sign = 1
    if s.startswith("-"):
        s = s[1:]
        sign = -1
    n = 0
    for c in s:
        assert c in "0123456789"
        n = n * 10 + (ord(c) - ord("0"))
    return n * sign

def test_parse_single_digit():
    for c in "0123456789":
        assert parse(c) == ord(c) - ord("0")


def test_parse_multiple_digits():
    assert parse("123") == 123

def test_parse_negative_numbers():
    assert parse("-123") == -123

