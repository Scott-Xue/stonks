import sys
import loader

if __name__ == '__main__':
    filename = sys.argv[1]
    tickers = loader.load(filename)
