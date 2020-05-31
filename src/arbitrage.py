class Query (object):

    def __init__(self, limit=0, stock_names=None, api=None):
        self.limit = limit
        self.names = stock_names
        self.api = api

    def pull(self, stock):
        """Connects to API to pull data for a given stock and returns a StockData object."""
        return

    def check(self, expiry_dates=None, strike_prices=None, underlying_cost=None):
        """Checks to see if there exists an expiry date for which
        the arbitrage formula for options holds"""
        result = False
        for expiry in expiry_dates:
            diff_cost = abs(strike_prices[expiry][0] - strike_prices[expiry][1])
            if diff_cost / underlying_cost > self.limit:
                result = True
        return result

    def find_opportunities(self):
        """Prints the stocks that satisfy the arbitrage opportunity requirements"""
        for name in self.names:
            data = self.pull(name)
            expiry_dates = data.get_dates()
            underlying_cost = data.get_underlying()
            strike_prices = data.get_strike_prices()
            if self.check(expiry_dates, strike_prices, underlying_cost):
                print(name)

class HistoricalQuery(Query):
    def __init__(self, timeframe):
        super().__init__()
        self.timeframe = timeframe
    
    def pull(self, stock, time):
        """Connects to a API to get historical data"""
        return

    def find_opportunities(self):
        for i in range(len(self.timeframe)):
            for j in range(i, len(self.timeframe)):
                for name in self.names:
                    underlying_time = self.timeframe[i]
                    option_time = self.timeframe[j]
                    underlying_cost = self.pull(name, underlying_time).get_underlying()
                    option_data = self.pull(name, option_time)
                    expiry_dates = option_data.get_dates()
                    strike_prices = option_data.get_strike_prices()
                    if self.check(expiry_dates, strike_prices, underlying_cost):
                        print(name, underlying_time, option_time)
            
class StockData(object):
    def __init__(self, name):
        self.name = name

    def get_dates(self):
        """Returns a list of expiry dates for put/call options"""
        return None

    def get_underlying(self):
        """Returns the spot price of this security"""
        return None

    def get_strike_prices(self):
        """Returns a dict mapping expiry dates to a tuple (call, put)
        prices for at-the-money options"""
        return None

class API(object):
    def __init__(self, args=None):
        self.name = args
