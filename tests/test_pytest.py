import pytest
from main import multiplication_int, multiplication_string


class TestFunctions:
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_multiplication_int(self):
        assert multiplication_int(2, 2) == 4

    def test_multiplication_string(self):
        assert multiplication_string('a', 4) == 'aaaa'

    @pytest.mark.parametrize("a, b, result", [(2, 3, 6), (-1, 1, -1)])
    def test_many(self, a, b, result):
        assert multiplication_int(a, b) == result
