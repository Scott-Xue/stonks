import sys

import loader

if __name__ == '__main__':
    args = sys.argv[1]
    tickers = loader.load(args)
