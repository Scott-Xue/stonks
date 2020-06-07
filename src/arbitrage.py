class Query (object):

    def __init__(self, limit=0, stock_names=None, api=None):
        self.limit = limit
        self.names = stock_names
        self.api = api

    def pull(self, stock_name):
        """Connects to API to pull data for a given stock and returns a StockData object."""
        return self.api.get(stock_name)

    def check(self, expiry_dates=None, option_prices=None, underlying_cost=None):
        """Checks to see if there exists an expiry date for which
        the arbitrage formula for options holds"""
        result = False
        for expiry in expiry_dates:
            diff_cost = abs(option_prices[expiry][0] - option_prices[expiry][1])
            if diff_cost / underlying_cost > self.limit:
                result = True
        return result

    def find_opportunities(self):
        """Prints the stocks that satisfy the arbitrage opportunity requirements"""
        buffer = []
        for name in self.names:
            data = self.pull(name)
            expiry_dates = data.get_dates()
            underlying_cost = data.get_underlying()
            option_prices = data.get_option_prices()
            if self.check(expiry_dates, option_prices, underlying_cost):
                buffer.append(name)
        return buffer
        
class HistoricalQuery(Query):
    def __init__(self, timeframe, limit=0, stock_names = None, api = None):
        super().__init__(limit, stock_names, api)
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
                    option_prices = option_data.get_option_prices()
                    if self.check(expiry_dates, option_prices, underlying_cost):
                        print(name, underlying_time, option_time)
            
class StockData(object):
    def __init__(self, name, dates, spot, option_prices):
        self.name = name
        self.dates = dates
        self.spot = spot
        self.option_prices = option_prices
    def get_dates(self):
        """Returns a list of expiry dates for put/call options"""
        return self.dates

    def get_underlying(self):
        """Returns the spot price of this security"""
        return self.spot

    def get_option_prices(self):
        """Returns a dict mapping expiry dates to a tuple (call, put)
        prices for at-the-money options"""
        return self.option_prices

class API(object):
    def __init__(self, args=None):
        self.name = args

class FakeAPI(API):
    def __init__(self, data):
        self.data = data
    
    def get(self, name):
        return self.data[name]