import unittest
from arbitrage import loader


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stocks = loader.load('test1.csv')
        self.assertEqual(stocks, ['one', 'two', 'three'])

if __name__ == '__main__':
    unittest.main()
