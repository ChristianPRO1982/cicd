import pytest
from math1 import add, sub


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(10, 100) == 110

def test_sub():
    assert sub(2, 3) == -1
    assert sub(-1, 1) == -2
    assert sub(0, 0) == 0
    assert sub(10, 100) == -90