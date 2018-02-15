# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 08:39:01 2018

@author: Guangzhuan Mo
"""

import pandas as pd
import numpy as np

# set for utilize the examples in the book
pd.set_option('display.notebook_repr_html', False);
pd.set_option('display.max_columns', 8);
pd.set_option('display.max_rows', 8);


# CREATING A Series AND ACCESSING ELEMENTS

#===========================================

# there are five way to access elements
# when creating without specifing index, pandas will use integer by default
# even if you specified a label index, you can still access elements of a Series by integer index

# s[index]
# s[index1: index2] : accessing element from [index1, index2) 
# s[ [index1, index2, index3, ... ]]
# s.head()
# s.tail()
# s.index  , display the (label) index of the Series
# s.values, dispay all the elements of a Series in the way of 'array([....])'

np.random.seed(1);
s = pd.Series(np.random.randn(30));


# setting the index labels at the time of construction, 
# using the index property
# or a Python dictionary
s2 = pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd']);
s3 = pd.Series( { 'a':1, 'b': 2, 'c': 3, 'd':4, 'e': 5} );

# sets the index labels after creation
# using the .index property
# different elements can have same label,
#
s4 = pd.Series(np.random.randn(5));     
s4.index = ['k', 'k', 'j', 'm','n'];    


#SIZE, SHAPE, UNIQUESS, COUNTS OF VALUES
# s = pd.Series([c, np.nan]);
# len(s)
# s.shape
# s.count() + 1 = len(s)
# s.value_counts()
# s.unique()

# ALIGNMENT  VIA INDEX LABELS
# NumPy ndarray : operate elements on the same position
# Series: operate elements with same Index labels


#CREATING A DataFrame
# think of spreadsheet/ database table/ n-dimension array

# create a DataFrame from a 2-d Numpy array
df = pd.DataFrame(np.array( [  [10, 11], [20, 21]  ] ));

# initialize by passing a list of Seriers objects

df1 = pd.DataFrame(
            [
                    pd.Series(np.arange(10, 15)),
                    pd.Series(np.arange(15, 20))
            ]
        );


# shape of a DataFrame
# df1.shape

# column names
df2 = pd.DataFrame(  np.array( [ [3,5],[8,5] ]), columns = ['a', 'b']        );
df2.columns = ['c','d'];

# row names
df2.index = ['r1', 'r2']


# vertically definition/ horizontal definition, 
# if there are index label for each series, 
# elements will be align automatically
s5 = pd.Series(np.arange(1, 6, 1));
s5.index = ['a', 'b', 'c', 'k', 'j'];
s6 = pd.Series(np.arange(6,11, 1));
s6.index = ['d', 'e', 'f', 'g', 'h']
df3 = pd.DataFrame( {  'c1' : s5, 'c2' : s6 } );
df4 = pd.DataFrame( [s5, s6]);
