import unittest
from main import multiplication_int, multiplication_string


class TestFunctions(unittest.TestCase):
    def setUp(self):
        print('setUp - work')

    def tearDown(self):
        print('tearDown - work')

    @classmethod
    def setUpClass(cls):
        print('setUpClass - work')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass - work')

    def test_multiplication_int(self):
        self.assertEqual(multiplication_int(2, 2), 4)

    @unittest.skipIf(multiplication_int(1, 1), 'эти параметры не примлемы')
    def test_multiplication_int_skip(self):
        self.assertEqual(multiplication_int(2, 2), 4)

    @unittest.skipUnless(multiplication_int(1, 2), 'эти параметры выжны')
    def test_multiplication_int_skip_unless(self):
        self.assertEqual(multiplication_int(1, 2), 2)

    @unittest.expectedFailure
    def test_multiplication_int_failure(self):
        self.assertEqual(multiplication_int(2, 2), 5)
