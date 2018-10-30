from mysoftware import *
import pytest

def test_square_integers():
    assert square(2) == 4
    assert square(0) == 0
    assert square(1) == square(-1)
    assert square(3) == 9

def test_add():
    assert 2+2 == 4

@pytest.mark.slow
def test_slow():
    print("Hello")
