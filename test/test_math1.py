import pytest
from math1 import add


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(10, 100) == 110
    assert add(900, 100) == 1000
