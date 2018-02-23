# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:33:11 2018


quandl key
YrRSzbzMY5qNvMWKHC9e
@author: Guangzhuan Mo
"""

import zipline as zp
import pandas as pd

from datetime import datetime
import pytz
from collections import OrderedDict

"""
The following algorithm implements a double moving average cross 
over. Investments will be made whenever the short moving average 
moves across the long moving average. We will trade only at the 
cross, not continuously buying or selling until the next cross. 
If trending down, we will sell all of our stock.  If trending up, 
we buy as many shares as possible up to 100. The strategy will 
record our buys and sells in extra data return from the simulation.
"""
class DualMovingAverage(zp.TradingAlgorithm):
    def initialize(context):
        # we need to track two moving averages, so we will set
        #these up in the context the .add_transform method 
        # informs zipline to execute a transform on every day 
        # of trading
        
        # the following will set up a MovingAverge transform, 
        # named short_mavg, accessing the .price field of the 
        # data, and a length of 100 days
        context.add_transform(zp.transforms.MovingAverage, 
                              'short_mavg', ['price'],
                              window_length=100)

        # and the following is a 400 day MovingAverage
        context.add_transform(zp.transforms.MovingAverage,
                              'long_mavg', ['price'],
                              window_length=400)

        # this is a flag we will use to track the state of 
        # whether or not we have made our first trade when the 
        # means cross.  We use it to identify the single event 
        # and to prevent further action until the next cross
        context.invested = False

    def handle_data(self, data):
        # access the results of the transforms
        short_mavg = data['AAPL'].short_mavg['price']
        long_mavg = data['AAPL'].long_mavg['price']
        
        # these flags will record if we decided to buy or sell
        buy = False
        sell = False

        # check if we have crossed
        if short_mavg > long_mavg and not self.invested:
            # short moved across the long, trending up
            # buy up to 100 shares
            self.order_target('AAPL', 100)
            # this will prevent further investment until 
            # the next cross
            self.invested = True
            buy = True # records that we did a buy
        elif short_mavg < long_mavg and self.invested:
            # short move across the long, tranding down
            # sell it all!
            self.order_target('AAPL', -100)
            # prevents further sales until the next cross
            self.invested = False
            sell = True # and note that we did sell

        # add extra data to the results of the simulation to 
        # give the short and long ma on the interval, and if 
        # we decided to buy or sell
        self.record(short_mavg=short_mavg,
                    long_mavg=long_mavg,
                    buy=buy,
                    sell=sell)


start = datetime(1990, 1, 1)
end = datetime(2017,1,1)
symbol = "AAPL"
src =  'google'
        
data = OrderedDict()
data['AAPL'] = pd.read_csv('aapl_19900101_2017_0101.csv', index_col=0, parse_dates=['Date'])
print (data['AAPL'].head())
type(data['AAPL'])

# convert DataFrame to Panel
panel = pd.Panel(data)
panel.minor_axis = ['Open', 'High', 'Low', 'Close', 'Volume']
panel.major_axis = panel.major_axis.tz_localize(pytz.utc)


sub_data = panel['2002-02-03': '2003-02-03']
