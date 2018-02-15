# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 09:33:12 2018

@author: Guangzhuan Mo
"""

import pandas as pd

# read data from file
# sp500.index
sp500 = pd.read_csv( "sp500.csv",
                    index_col = 'Symbol',
                    usecols = ['Symbol', 'Sector', 'Price', 'Book Value']);
                    
# sp500 = pd.read_csv( "sp500.csv",index_col = 'Symbol',usecols = [0,2,3,7]);

# SELECT COLUMNS OF A DataFrame

# sp500[ [1, 2] ].head();
# sp500['Sector'];
# sp500['Sector', 'Price'];
# sp500.Price;

# SELECT ROWS 

# slicing using the [] operator, NOT RECOMMENDED
# sp500[:3]  
# sp500['XYL' : 'YUM'];    

# selecting rows by the index label and location .loc[] and .iloc[], RECOMMENDED
# sp500.loc['MMM']
# sp500.loc[ ['MMM', 'MSFT' ] ]
# sp500.iloc[ [0, 2] ]

# i1 = sp500.index.get_loc('MMM');
# i2 = sp500.index.get_loc('A');
#sp500.iloc[ [i1, i2] ]                    
                    
#sp500.ix[ ['MMM', 'MSFT'] ];
#sp500.ix[ [10, 200, 450] ]                    

#Scalar lookup by label of location using .at[], and .iat[]
# DF.at['row label', 'column lable']
# sp500.at['MMM', 'Price];   
# DF.iat[row_index, column_index]
# sp500.iat[ 0,1 ]                 

# selecting rows using the boolean selection
# sp500.Price < 100
# sp500[sp500.Price < 100]    

# sp500[ (sp500.Price < 10) & (sp500.Price > 0)] [ ['Price'] ]        