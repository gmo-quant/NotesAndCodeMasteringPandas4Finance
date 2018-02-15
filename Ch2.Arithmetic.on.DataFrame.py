# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:07:01 2018

@author: Guangzhuan Mo
"""

import numpy as np;
import pandas as pd;

np.random.seed(123456)
df = pd.DataFrame(np.random.randn(5, 4), columns = ['A', 'B', 'C', 'D'])

df1 = df * 2
df2 = df1 -df.iloc[0]

subframe = df[1:4][ ['B', 'C']]
df3 = df2 - subframe;
a_col = df['A'];
df4 = df.sub(a_col, axis=0);
