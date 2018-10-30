from mysoftware import *
import pytest

def test_coulomb():
    assert coulomb(5) == 1/5
    assert coulomb(-1) == 1
    assert coulomb(2.) == 0.5
    with pytest.raises(ValueError):
        coulomb(0)
    with pytest.raises(AssertionError):
        coulomb('a')
