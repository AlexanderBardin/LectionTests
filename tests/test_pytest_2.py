import pytest
from main import multiplication_int, multiplication_string


def test_multiplication_int():
    assert multiplication_int(2, 2) == 4


def test_multiplication_string():
    assert multiplication_string('a', 4) == 'aaaa'
