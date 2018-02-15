# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:24:14 2018

@author: Guangzhuan Mo
"""

import numpy as np
import pandas as pd

pd.set_option('display.notebook_repr_html', False);
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 8)
pd.set_option('precision', 7)

#import datetime
from datetime import datetime
#import matplotlib.pyplot as plt


#time-series data and the Datetimeindex

dates = [datetime(2014, 8,1), datetime(2014, 8, 2)];
dti = pd.DatetimeIndex(dates);
dti2 = pd.to_datetime(['Aug 1, 2014', '2014-08-02', '2014/8/3', None, '8/3/2014']);

np.random.seed(123456);
ts = pd.Series(np.random.randn(2), dates)
ts1 = pd.Series(np.random.randn(5), dti2);

#import pandas_datareader as web
src = "google"
start = '2012-1-1'
end = '2013-12-30'
#msft = web.DataReader("MSFT", src, start, end);
#msft.to_csv('msft-20120101-20131230.csv')
msft = pd.read_csv("msft-20120101-20131230.csv", index_col = 0, parse_dates=True)
msftC = msft['Close']
msftCc = msft[['Close']]

#Creating time-series with specific frequencies

bymin = pd.Series(np.arange(0, 90*60*24), pd.date_range('2014-08-01', '2014-10-29 23:59:00', freq = 'T'))

#representing intervals of time using periods.

aug2014 = pd.Period('2014-08', freq = 'M')


