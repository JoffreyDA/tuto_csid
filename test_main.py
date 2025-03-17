# test_main.py
from main import add, prout


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_prout():
    assert prout(2) == 4
    assert prout(3) == 9
    assert prout(0) == 0