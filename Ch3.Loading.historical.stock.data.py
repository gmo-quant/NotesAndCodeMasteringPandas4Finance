# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 13:13:05 2018

@author: Guangzhuan Mo
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

pd.set_option('display.notebook_repr_html', False);
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 8)
pd.set_option('precision', 3)


import pandas_datareader as web
start = datetime.datetime(2012, 1, 1);
end = datetime.datetime(2012, 12, 30);

src = 'google'
#msft = web.DataReader("MSFT", src, start, end);
#aapl = web.DataReader("AAPL", src, start, end);

#msft.to_csv("msft.csv");
#aapl.to_csv("aapl.csv");

msft = pd.read_csv("msft.csv", index_col = 0, parse_dates=True)
aapl = pd.read_csv("aapl.csv", index_col = 0, parse_dates=True)

#REORGANIZING AND RESHAPING DATA


# CONCATENATING MULTIPLE DataFrame OBJECTS

msftA01 = msft['2012-01']['Close']
msftA02 = msft['2012-02']['Close']

#aaplA01 = aapl['2012-01'] [ ['Close'] ]
aaplA01 = aapl['2012-01'] [ 'Close' ]
withDups = pd.concat ( [msftA01[:3], aaplA01[:3]])

closes = pd.concat( [msftA01[:3], aaplA01[:3]], keys = ['MSFT', 'AAPL']);


msftAV = msft[ ['Close', 'Volume'] ]
aaplAV = msft[ ['Close', 'Volume'] ]
cma = pd.concat( [msftAV, aaplAV]);

aaplA = aapl[['Close']].rename( columns = {"Close": "aapl"})
mc = pd.concat( [msftAV, aaplA])
minner = pd.concat ( [msftAV, aaplA], join='inner')


msftA = msft[['Close']].rename( columns = {"Close": "msft"})
closes_col = pd.concat( [msftA, aaplA], axis = 1)


msftA1 = msft[['Close', 'Volume']]
aaplA1 = aapl[['Close', 'Volume']]
close = pd.concat( [msftA1, aaplA1], axis = 1, keys = ['MSFT', 'AAPL']);