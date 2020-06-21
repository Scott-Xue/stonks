import sys
import loader
import arbitrage

if __name__ == '__main__':
    filename = sys.argv[1]
    tickers = loader.load(filename)
    if len(sys.argv) > 2:
        timeframe = sys.argv[2]
        hquery = arbitrage.HistoricalQuery(tickers, timeframe)
    else:
        query = arbitrage.Query(stock_names=tickers)
        buffer = query.find_opportunities()
        print(buffer)
