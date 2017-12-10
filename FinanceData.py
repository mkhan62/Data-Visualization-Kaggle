import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web
import seaborn as sns
import matplotlib.pyplot as plt


start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

# DataFrames of Stock Information
BAC = web.DataReader("BAC", 'yahoo', start, end)  # Bank of America
C = web.DataReader("C", 'yahoo', start, end)  # CitiGroup
GS = web.DataReader("GS", 'yahoo', start, end)  # Goldman Sachs
JPM = web.DataReader("JPM", 'yahoo', start, end)  # JPMorgan Chase
MS = web.DataReader("MS", 'yahoo', start, end)  # Morgan Stanley
WFC = web.DataReader("WFC", 'yahoo', start, end)  # Wells Fargo

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], keys=tickers, axis=1)  # joining all DataFrames
bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']
print(bank_stocks.xs('Close', level=1, axis=1).max())  # Max Close price for each bank stock throughout the period


returns = pd.DataFrame(index=bank_stocks.index, columns=tickers)
for x in tickers:
    column = bank_stocks.xs('Close', level=1, axis=1)[x].pct_change()  # populated returns DataFrame
    returns[x] = column

# sns.pairplot(returns[1:])
worst = returns.idxmin()
best = returns.idxmax()
sns.set_style('whitegrid')
sns.distplot(returns.ix['2015-01-01':'2015-12-31']['BAC'], bins=30)
plt.show()

bank_stocks.xs('Close', level=1, axis=1).plot(figsize=(12, 4))
plt.legend()
plt.show()

sns.clustermap(bank_stocks.xs('Close', axis=1, level=1).corr(), annot=True)
plt.show()
