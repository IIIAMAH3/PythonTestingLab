import pytest
from calculator import add

def test_add_with_fixture(numbers):
    a, b, expected = numbers
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 0, 0)])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected