import sys
import unittest
from arbitrage import loader


class MyTestCase(unittest.TestCase):
    def test_something(self):
        parent_dir = sys.path[0]
        stocks = loader.load(parent_dir + '/tests/test1.csv')
        self.assertEqual(stocks, ['NASDAQ:AAPL', 'NASDAQ:EA', 'NSYE:AXE'])

if __name__ == '__main__':
    unittest.main()
