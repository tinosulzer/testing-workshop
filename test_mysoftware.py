from mysoftware import *
import pytest

def test_square_integers():
    assert square(2) == 4
    assert square(0) == 0
    assert square(1) == square(-1)
    assert square(3) == 9

def test_coulomb():
    assert coulomb(5) == 1/5
    assert coulomb(-1) == 1
    assert coulomb(2.) == 0.5
    with pytest.raises(ValueError):
        coulomb(0)
    with pytest.raises(AssertionError):
        coulomb('a')
