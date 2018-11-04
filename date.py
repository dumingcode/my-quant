# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:44:38 2018

@author: Administrator
"""
def ten_year_calc(num,start_date):
    yearLen = timedelta(days=365)
    for x in range(num):
        print(start_date + yearLen*x)

    

from datetime import date
from datetime import timedelta
import pandas as pd

d = date(2007, 11, 5)
print(d.isoformat())
ten_year_calc(10, d)


s= '4545,6565'.split(',')
print(s[0])

arr = []
arr.append(1)
arr.append(2)
print(arr)
      
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame()