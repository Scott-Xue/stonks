import json
import io
import unittest
import unittest.mock
from src import arbitrage


class QueryTest(unittest.TestCase):
    def setUp(self):
        self.dates = ["01/01/1990", "01/02/1990"]
        self.spot = 10
        self.option_prices = {"01/01/1990" : (15, 15), "01/02/1990" : (14, 15)}
        self.stock = arbitrage.StockData("AAPL", self.dates, self.spot, self.option_prices)
        self.data = {"AAPL" : self.stock}
        self.names = ["AAPL"]
        self.api = arbitrage.FakeAPI(self.data)
        
    def test_check(self):
        q = arbitrage.Query(stock_names=self.names, api = self.api)
        self.assertTrue(q.check(self.dates, self.option_prices, self.spot))

    def test_find_opportunities(self):
        q = arbitrage.Query(stock_names=self.names, api = self.api)
        result = q.find_opportunities()
        self.assertListEqual(result, ["AAPL"])

class StockDataTest(unittest.TestCase):
    def setUp(self):
        return None


class APITest(unittest.TestCase):
    def setUp(self):
        self.api = arbitrage.API()

    def test_get_option_expirations(self):
        pass

    def test_get_option_chain(self):
        pass

    def test_doesnt_exist(self):
        pass

if __name__ == '__main__':
    unittest.main()
