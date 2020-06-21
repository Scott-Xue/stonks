import unittest
import unittest.mock
from src import arbitrage


class QueryTest(unittest.TestCase):
    def setUp(self):
        self.dates = ["01/01/1990", "01/02/1990"]
        self.spot = 10
        self.option_prices = {"01/01/1990": {"call": 15, "put": 15, "strike": 10},
                              "01/02/1990": {"call": 14, "put": 15, "strike": 10}}
        self.stock = arbitrage.StockData("AAPL", self.dates, self.spot, self.option_prices)
        self.data = {"AAPL": self.stock}
        self.names = ["AAPL"]
        self.api = arbitrage.FakeAPI(self.data)

    def test_check(self):
        q = arbitrage.Query(stock_names=self.names, api=self.api)
        self.assertNotEqual(q.check(self.dates, self.option_prices, self.spot), [])

    def test_check_false(self):
        new_options = {"01/01/1990": {"call": 15, "put": 14, "strike": 9},
                       "01/02/1990": {"call": 15, "put": 15, "strike": 10}}
        new_data = arbitrage.StockData("VXX", self.dates, self.spot, new_options)
        new_api = arbitrage.FakeAPI(new_data)
        q = arbitrage.Query(stock_names=["VXX"], api=new_api)
        self.assertEqual(q.check(self.dates, new_options, self.spot), [])

    def test_check_all_scenarios(self):
        '''scenario_1a: strike > spot, put > call, no opportunities
           scenario_1b: strike > spot, put > call, opportunities
           scenario_2: strike > spot, put < call
           scenario_3: strike < spot, put > call
           scenario_4a: strike < spot, put < call, no opportunities
           scenario_4b: strike < spot, put < call, opportunities'''
        date = "01/02/1990"
        new_dates = [date]
        q = arbitrage.Query(stock_names=["VXX"])
        spot1, spot2 = 9, 10

        scenario_1a = {date: {"call": 4, "put": 5, "strike": 10}}
        self.assertEqual(q.check(new_dates, scenario_1a, spot1), [])

        scenario_1b = {date: {"call": 4, "put": 5, "strike": 11}}
        self.assertEqual(q.check(new_dates, scenario_1b, spot1), [(date, 1)])

        scenario_2 = {date: {"call": 5, "put": 4, "strike": 10}}
        self.assertEqual(q.check(new_dates, scenario_2, spot1), [(date, 2)])

        scenario_3 = {date: {"call": 4, "put": 5, "strike": 9}}
        self.assertEqual(q.check(new_dates, scenario_3, spot2), [(date, 2)])

        scenario_4a = {date: {"call": 5, "put": 4, "strike": 9}}
        self.assertEqual(q.check(new_dates, scenario_4a, spot2), [])

        scenario_4b = {date: {"call": 5, "put": 4, "strike": 8}}
        self.assertEqual(q.check(new_dates, scenario_4b, spot2), [(date, 1)])

    def test_find_opportunities(self):
        q = arbitrage.Query(stock_names=self.names, api=self.api)
        result = q.find_opportunities()
        self.assertEqual(result[0][0], "AAPL")


class StockDataTest(unittest.TestCase):
    def setUp(self):
        return None


class TradierAPITest(unittest.TestCase):
    def setUp(self):
        self.api = arbitrage.TradierAPI()
        self.expiries = self.api.get_expiries("VXX")
        self.spot = self.api.get_spot_price("VXX")

    def test_get_expiries(self):
        self.assertTrue(isinstance(self.expiries, list))

    def test_get_spot_price(self):
        self.assertTrue(isinstance(self.spot, float))

    def test_get_option_premiums(self):
        curr = self.api.get_option_premiums("VXX", self.expiries[0], self.spot)
        self.assertTrue(isinstance(curr, dict))

    def test_get_stock_data(self):
        stock = self.api.get_stock_data("VXX")
        self.assertTrue(isinstance(stock, arbitrage.StockData))


if __name__ == '__main__':
    unittest.main()
