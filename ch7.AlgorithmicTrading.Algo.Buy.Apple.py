# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:04:02 2018

@author: Guangzhuan Mo

Algorithm - buy apple
"""


import pandas as pd
import zipline as zp
import zipline.utils.factory as zpf
import zipline.data.loader as zl # yahoo_finance is depreciated
from datetime import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
import pytz
from collections import OrderedDict


class BuyApple(zp.TradingAlgorithm):
    trace = False
    
    def __init__(self, trace = False):
        BuyApple.trace = trace
        super(BuyApple, self).__init__()
        
    def initialize(context):
        if BuyApple.trace: print("--->initialize")
        if BuyApple.trace: print(context)
        if BuyApple.trace: print("<--- initialize")
        
    def handle_data(self, context):
        if BuyApple.trace: print("-->handle_data")
        if BuyApple.trace: print(context)
       # self.order("AAPL", 1)
        if BuyApple.trace: print("<--- handle_data")
        if BuyApple.trace : print("<--- handle_data")
  

start = datetime(1990, 1, 1)
end = datetime(2017,1,1)
symbol = "AAPL"
src =  'google'


#aapl = web.DataReader(symbol, src, start, end);
#aapl.to_csv("aapl_19900101_2017_0101.csv");
#aapl = pd.read_csv("aapl_19900101_2017_0101.csv", index_col = 0, parse_dates=['Date'])
#aapl.plot(figsize=(1000, 500))






data = OrderedDict()
data['AAPL'] = pd.read_csv('aapl_19900101_2017_0101.csv', index_col=0, parse_dates=['Date'])
print (data['AAPL'].head())
type(data['AAPL'])

# convert DataFrame to Panel
panel = pd.Panel(data)
panel.minor_axis = ['Open', 'High', 'Low', 'Close', 'Volume']
panel.major_axis = panel.major_axis.tz_localize(pytz.utc)




    