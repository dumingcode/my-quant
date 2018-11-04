# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:44:38 2018

@author: duming
"""


    
import pandas as pd
import matplotlib.pyplot as plt
from basic_units import cm, inch


def plt_income(arr,bins):
    bottom = 0 * cm
    width = 0.8 * cm
    plt.bar( bins,arr,label='总利润')
    plt.xlabel('时间')
    plt.ylabel('总利润')
    plt.show()

income_pd = pd.read_csv('../data/income.csv',index_col=0)
#print(income_pd.loc[:,'000016'])
print(income_pd['000016'].values.tolist())
print(income_pd['000016'].index.tolist())
plt_income(income_pd['000016'].values.tolist(),income_pd['000016'].index.tolist())
plt_income(income_pd['399905'].values.tolist(),income_pd['399905'].index.tolist())
plt_income(income_pd['000932'].values.tolist(),income_pd['000932'].index.tolist())












