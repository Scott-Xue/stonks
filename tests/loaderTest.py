import sys
import unittest
from src import loader


class loaderTest(unittest.TestCase):
    def test_reads_properly(self):
        parent_dir = sys.path[0]
        stocks = loader.load(parent_dir + '/tests/test1.csv')
        self.assertEqual(stocks, ['NASDAQ:AAPL', 'NASDAQ:EA', 'NSYE:AXE'])

    def test_errors_on_wrong_path(self):
        parent_dir = sys.path[0]
        self.assertRaises(AssertionError,
                          lambda: loader.load(parent_dir + 'nosuchfile'))

if __name__ == '__main__':
    unittest.main()
