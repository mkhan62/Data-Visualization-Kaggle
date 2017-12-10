import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

# DataFrames of Stock Information
BAC = web.DataReader("BAC", 'quandl', start, end)  # Bank of America
C = web.DataReader("C", 'quandl', start, end)  # CitiGroup
GS = web.DataReader("GS", 'quandl', start, end)  # Goldman Sachs
JPM = web.DataReader("JPM", 'quandl', start, end)  # JPMorgan Chase
MS = web.DataReader("MS", 'quandl', start, end)  # Morgan Stanley
WFC = web.DataReader("WFC", 'quandl', start, end)  # Wells Fargo

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], keys=tickers, axis=1)  # joining all DataFrames
bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']
print(bank_stocks.head())
