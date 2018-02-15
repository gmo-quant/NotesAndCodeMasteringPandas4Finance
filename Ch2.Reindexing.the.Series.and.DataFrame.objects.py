# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:29:44 2018

@author: Guangzhuan Mo
"""

"""
the process of performing a reindex does the following:
    
    reorders existing data to match a set of labels
    inserts NaN markers where no data exists for a label
    fills missing data for a label using a type of logic ( defaulting to adding NaNs)
"""

import numpy as np
import pandas as pd
np.random.seed(1)
s = pd.Series(np.random.randn(5))
s.index = ['a', 'b', 'c', 'd', 'e']
s2 = s.reindex(['a', 'c', 'e', 'g'])
s2['a'] = 0

s3 = pd.Series( [0, 1, 2], index = [0, 1, 2])
s4 = pd.Series( [3, 4, 5], index = ['0', '1', '2'])

s4.index = s4.index.values.astype(int)

s5 = s.copy()
s6 = s5.reindex(['a', 'f'], fill_value=0)

s7 = pd.Series( ['red', 'green', 'blue'], index=[0,3,5])
s8 = s7.reindex(np.arange(0, 7), method = 'ffill')
s9 = s7.reindex(np.arange(0, 7), method = 'bfill')
