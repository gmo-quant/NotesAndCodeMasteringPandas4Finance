# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:44:01 2018

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

msftA = msft['2012-01']['Close']

msftAR = msftA.reset_index()
msftVR = msft[['Volume']].reset_index()

