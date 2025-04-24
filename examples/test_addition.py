# example TDD code

from addition import add

def test_addition():
    """
    Testing addition
    """
    print("test_addition")
    assert add(1,2) == 3

def test_float_addition():
    print("test_float_addition")
    assert -0.00001 < (add(0.66666, 0.33333) - 0.99999) < 0.00001

if __name__ == "__main__":
    test_addition()
    test_float_addition()
    print("testing done")

