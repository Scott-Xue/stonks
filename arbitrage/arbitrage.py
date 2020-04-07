class Query (object):

    def __init__(self, limit, stock_name):
        self.limit = limit
        self.name = stock_name

    def pull(self):
        """Connects to API to pull data for a given stock"""
        return

    def check(self, expiry_dates=None, diff_cost=None, underlying_cost=None):
        """Checks to see if there exists an expiry date for which
        the arbitrage formula for options holds"""
        result = False
        for expiry in expiry_dates:
            if diff_cost / underlying_cost > self.limit:
                result = True
        return result
