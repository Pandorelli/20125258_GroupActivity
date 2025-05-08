import pytest
import example


def test_subtract():
    assert example.subtract(1, 2) == -1


def test_add():
    assert example.add(2, 3) == 5
    assert example.add('space', 'ship') == 'spaceship'


# uncomment the following test in step 5
def test_subtract1():
    assert example.subtract(2, 3) == -1
