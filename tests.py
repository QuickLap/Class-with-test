import unittest
from testunittest import *

class TestMy_programm(unittest.TestCase):
    def test_1(self):
        with self.subTest():
            self.assertEqual(count_sum_digits(123),3,"not  = 3")
            self.assertEqual(count_sum_digits(193), 12, "not  = 3")

class TestMy_programm(unittest.TestCase):
    def setUp(self):
        self.park = New_park()
        self.park.adding('Lake')
        self.park.adding('House')
        self.park.adding('Castle')
        self.park.adding('Japanese temple')
    def TearDown(self):
        del self.park

    def test_1(self):
        self.assertEqual(self.park.count_things(),4,'Error not equal')

    def test_2(self):
        self.assertEqual(self.park.last_item(),'Japanese temple','Error not POP')

    def test_3(self):
        x = self.park.count_things()
        self.park.deleting_named('Castle')
        self.assertEqual(self.park.count_things()+1, x, 'Error not POP')

    def test_4(self):
        x = self.park.count_things()
        self.park.deleting_last()
        self.assertEqual(self.park.count_things()+1, x, 'Error not POP')

if __name__ == '__main__':
    unittest.main()