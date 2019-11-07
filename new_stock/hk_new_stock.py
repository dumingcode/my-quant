# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from datetime import date
from datetime import timedelta
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

path = os.path.abspath('.')
path += '\\data\\new_stock\\hk_new_stock.csv'
hk_new_stock = pd.read_csv(path,index_col=0,encoding='gbk')
hk_new_stock = hk_new_stock.dropna()

hk_new_stock = hk_new_stock[hk_new_stock['recommend'] != '不建议']

hk_new_stock['money'] = hk_new_stock['money'].astype(float)
print(hk_new_stock['money'].describe())
hk_new_stock['luck'] = hk_new_stock['luck'].str.strip("%").astype(float)/100
hk_new_stock['rise'] = hk_new_stock['rise'].str.strip("%").astype(float)/100
corr_pd = hk_new_stock[['money','luck','rise']]
print(corr_pd.corr())
hk_new_stock['earn'] = hk_new_stock['luck']*(hk_new_stock['money']* hk_new_stock['rise']-hk_new_stock['money']*(0.010077)-18-5)
print(hk_new_stock['earn'].describe())
print(hk_new_stock['earn'].sum())

all_data =  hk_new_stock['earn'].values.tolist()
# 绘制violin 和 box plot图
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 6))

# plot violin plot
axes[0].violinplot(all_data,
                   showmeans=False,
                   showextrema=True,
                   showmedians=True)
axes[0].set_ylabel('expected profit')
axes[0].set_title('Violin plot')

# plot box plot
axes[1].boxplot(all_data)
axes[1].set_title('Box plot')


plt.show()
# path1 = os.path.abspath('.')
# path1 += '\\data\\new_stock\\result.csv'
# hk_new_stock['earn'].to_csv(path1)
# print(hk_new_stock[['money','luck']].describe())