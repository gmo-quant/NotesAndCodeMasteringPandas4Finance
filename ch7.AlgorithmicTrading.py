# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:44:48 2018

@author: Guangzhuan Mo

Chapter 7 Algorithmic Trading
"""

"""
    Notebook setup
"""
import pandas as pd
import pandas_datareader as web
import numpy as np
import zipline as zp
import zipline.utils.factory as zpf

from datetime import datetime
import matplotlib.pyplot as plt

pd.set_option('display.notebook_repr_html', False);
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 78)
pd.set_option('precision', 6)

"""
symbal = "MSFT"
src  = "google"
start = datetime(2000, 1, 1)
end = datetime(2017,12,31)

msft = web.DataReader(symbal, src,start,end)
msft.to_csv("msft_2000_2017.csv")

"""

# calculate the rolling means using pd.rolling_mean()
# 7-day, 30-day, 90-day, 120-day rolling means during the same period
"""
msft['MA7'] = msft.Close.rolling(window =7, center = False).mean()
msft['MA30'] =msft.Close.rolling(window = 30, center = False).mean()
msft['MA90'] = msft.Close.rolling(window = 90, center = False).mean()
msft['MA120'] = msft.Close.rolling(window = 120, center = False).mean()
msft['MA240'] = msft.Close.rolling(window = 240, center = False).mean()

# plot the price versus various rolling means
msft['2014'][['Close', 'MA7', 'MA30', 'MA90', 'MA120', 'MA240']].plot(figsize = (24,16));
msft['2012'][['Close', 'MA7', 'MA30', 'MA90', 'MA120', 'MA240']].plot(figsize = (24,16));

"""

# the price of MSFT had a progressive rise over 2014, 
# and the 120-day rolling mean has functioned as a floor/supprot, 
# where the price bounces off this floor as it approaches it. 
# the longer the window of the rolling mean,
# the lower and smoother the floor will be in an uptrending market.

# exponentially weighted moving average.

#periods = 10
#alpha = 2.0/(periods + 1 )
#factors = (1-alpha ** np.arange(1,11))
#sum_factors = factors.sum()
#weights = factors/sum_factors

"""
msft = pd.read_csv("msft_2000_2017.csv", index_col = 0, parse_dates=True)
span = 90
msft_ewma =msft[['Close']].copy()
msft_ewma['MA90'] = msft_ewma.rolling(window = span, center = False).mean()
msft_ewma['EWMA90'] = msft_ewma['Close'].ewm(span=span)
msft_ewma['2014'][['Close', 'MA90', 'EWMA90']].plot(figsize=(24,16))
"""

"""
Crossovers
Technical analysis techniques
"""
msft = pd.read_csv("msft_2000_2017.csv", index_col = 0, parse_dates=True)
msft['MA30'] =msft.Close.rolling(window = 30, center = False).mean()
msft['MA90'] = msft.Close.rolling(window = 90, center = False).mean()
msft['2003-1' : '2003-9'][['Close', 'MA30', 'MA90']].plot(figsize=(24, 16))





