import unittest
import unittest.mock
from src import arbitrage
import requests


class QueryTest(unittest.TestCase):
    def setUp(self):
        self.dates = ["01/01/1990", "01/02/1990"]
        self.spot = 10
        self.option_prices = {"01/01/1990": (15, 15), "01/02/1990": (14, 15)}
        self.stock = arbitrage.StockData("AAPL", self.dates, self.spot, self.option_prices)
        self.data = {"AAPL": self.stock}
        self.names = ["AAPL"]
        self.api = arbitrage.FakeAPI(self.data)

    def test_check(self):
        q = arbitrage.Query(stock_names=self.names, api=self.api)
        self.assertTrue(q.check(self.dates, self.option_prices, self.spot))

    def test_find_opportunities(self):
        q = arbitrage.Query(stock_names=self.names, api=self.api)
        result = q.find_opportunities()
        self.assertListEqual(result, ["AAPL"])


class StockDataTest(unittest.TestCase):
    def setUp(self):
        return None


class APITest(unittest.TestCase):
    def setUp(self):
        self.api = arbitrage.API("tradier")

    def test_response(self):
        r = requests.get('https://sandbox.tradier.com/v1/markets/options/expirations',
                         params={'symbol': "VXX", 'includeAllRoots': 'true', 'strikes': 'false'},
                         headers={'Authorization': 'Bearer Bfo8MwBCA6lFOqWSdWIe1Ke7IigA', 'Accept': 'application/json'})
        self.assertTrue(r.ok)
        data = r.json()
        dates = data["expirations"]["date"]
        self.assertTrue(isinstance(dates, list))
        s = requests.get('https://sandbox.tradier.com/v1/markets/quotes',
                         params={'symbols': "AAPL", 'greeks': 'false'},
                         headers={'Authorization': 'Bearer Bfo8MwBCA6lFOqWSdWIe1Ke7IigA', 'Accept': 'application/json'})
        self.assertTrue(s.ok)
        self.assertTrue(type(s.json()["quotes"]["quote"]["ask"]) == float)
        t = requests.get('https://sandbox.tradier.com/v1/markets/options/chains',
                         params={'symbol': "VXX", 'expiration': dates[0], 'greeks': 'false'},
                         headers={'Authorization': 'Bearer Bfo8MwBCA6lFOqWSdWIe1Ke7IigA', 'Accept': 'application/json'})
        self.assertTrue(t.ok)
        ops = t.json()['options']['option']
        self.assertTrue(isinstance(ops, list))


if __name__ == '__main__':
    unittest.main()
