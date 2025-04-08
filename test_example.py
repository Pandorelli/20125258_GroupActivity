import pytest
import example


def test_subtract():
    assert example.subtract(1, 2) == 3

def test_add():
    assert example.add(2, 3) == 5
    assert example.add('space', 'ship') == 'spaceship'
