# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:00:49 2018

@author: Guangzhuan Mo
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt


# sql join 
pd.set_option('display.notebook_repr_html', False);
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 8)
pd.set_option('precision', 3)

msft = pd.read_csv("msft.csv", index_col = 0, parse_dates=True)
aapl = pd.read_csv("aapl.csv", index_col = 0, parse_dates=True)


msft.insert(0, 'Symbol', 'MSFT')
aapl.insert(0, 'Symbol', 'AAPL')

combined = pd.concat( [msft, aapl]).sort_index()
s4p = combined.reset_index();

closes = s4p.pivot(index = 'Date', columns = 'Symbol', values='Close')

melted = pd.melt(s4p, id_vars =['Date', 'Symbol'])

#melting
#grouping
#aggregating
#splitting
