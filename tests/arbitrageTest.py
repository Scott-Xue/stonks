import json
import unittest
from src import arbitrage


class QueryTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class StockDataTest(unittest.TestCase):
    def setUp(self):
        return None


class APITest(unittest.TestCase):
    def setUp(self):
        self.api = arbitrage.API()

    def test_get_option_expirations(self):
        option_expirations = self.api.get_option_expirations()
        with open("optionchain.json") as file:
            data = json.load(file)
        self.assertEqual(option_expirations, data)

    def test_get_option_chain(self):
        pass

    def test_doesnt_exist(self):
        pass

if __name__ == '__main__':
    unittest.main()
