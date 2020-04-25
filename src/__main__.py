import sys
import loader
import arbitrage

if __name__ == '__main__':
    filename = sys.argv[1]
    tickers = loader.load(filename)
    query = arbitrage.Query(tickers)
    query.find_opportunities()
