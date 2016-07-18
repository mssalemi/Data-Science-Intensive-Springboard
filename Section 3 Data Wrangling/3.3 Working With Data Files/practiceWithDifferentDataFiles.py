# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:49:08 2016

@author: mehdisalemi
"""

import pandas as pd
import numpy as np
from io import StringIO

df = pd.read_csv("military-surplus-gear.csv", index_col=None, usecols=["State","Quantity"])
print(df.head())

data = 'a,b,c\n1,2,3\n4,5,6\n7,8,9'
print(data)
df2 = pd.read_csv(StringIO(data))
print(df2)

