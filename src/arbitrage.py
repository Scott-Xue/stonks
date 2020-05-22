class Query (object):

    def __init__(self, limit=0, stock_names=None, api=None):
        self.limit = limit
        self.names = stock_names
        self.api = api

    def pull(self, stock):
        """Connects to API to pull data for a given stock"""
        return

    def check(self, expiry_dates=None, diff_costs=None, underlying_cost=None):
        """Checks to see if there exists an expiry date for which
        the arbitrage formula for options holds"""
        result = False
        for expiry in expiry_dates:
            diff_cost = diff_costs[expiry]
            if diff_cost / underlying_cost > self.limit:
                result = True
        return result

    def find_opportunities(self):
        """Prints the stocks that satisfy the arbitrage opportunity requirements"""
        for name in self.names:
            data = self.pull(name)
            expiry_dates = data.get_dates(name)
            underlying_cost = data.get_underlying(name)
            spot_prices = data.get_spot_prices(name)
            diff_costs = [x - underlying_cost for x in spot_prices]
            if self.check(expiry_dates, diff_costs, underlying_cost):
                print(name)

class StockData(object):
    def __init__(self, name):
        self.name = name

class API(object):
    def __init__(self, args=None):
        self.name = args
