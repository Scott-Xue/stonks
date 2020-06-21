import unittest
import sys
from src import loader, arbitrage


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.args = sys.path[0] + "/tests/test_main.csv"
        self.result = [("VXX", [("06/15/2020", 3), ("06/20/2020", 2)]),
                       ("AAPL", [("07/08/2020", 5)])]
        self.vxx_spot = 25
        self.aapl_spot = 200
        self.vxx_dates = ["05/20/2020", "06/15/2020", "06/20/2020"]
        self.aapl_dates = ["06/29/2020", "07/08/2020"]
        self.vxx_options = {"05/20/2020": {"call": 15, "put": 10, "strike": 20},
                            "06/15/2020": {"call": 18, "put": 10, "strike": 20},
                            "06/20/2020": {"call": 15, "put": 17, "strike": 25}}
        self.aapl_options = {"06/29/2020": {"call": 100, "put": 100, "strike": 200},
                             "07/08/2020": {"call": 105, "put": 100, "strike": 200}}
        self.vxx = arbitrage.StockData("VXX", self.vxx_dates, self.vxx_spot, self.vxx_options)
        self.aapl = arbitrage.StockData("AAPL", self.aapl_dates, self.aapl_spot, self.aapl_options)
        self.data = {"VXX": self.vxx, "AAPL": self.aapl}
        self.api = arbitrage.FakeAPI(self.data)

    def test_correct_opportunities(self):
        tickers = loader.load(self.args)
        q = arbitrage.Query(stock_names=tickers, api=self.api)
        buffer = q.find_opportunities()
        self.assertEqual(buffer, self.result)
