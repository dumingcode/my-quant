# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:44:38 2018
绘图计算各个指数的净利润增长情况
两张图分别展示净利润变化以及净利润增速变化
@author: duming
"""


    
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

def plt_income(arr,bins,index_name):
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['figure.figsize'] = (16.0, 4.0) # 设置figure_size尺寸
    fig, (ax0, ax1) = plt.subplots(ncols=2, sharex=True)
    ax0.set_title(index_name+'净利润总额变化(速度)')
    ax0.bar(bins,arr)
    ax1.set_title(index_name+'净利润增速变化(加速度)')
    ax1.plot(bins,year_ratio(arr))
    plt.savefig('../pic/index_profit/'+index_name, dpi=200) #指定分辨率
    plt.show()

# 计算同比增长率
def year_ratio(arr):
    pre = -1
    ratios = [0]
    for data in arr:
        if(pre != -1 and pre!=0):
            ratios.append((data-pre)/pre*100)
        if(pre == 0):
            ratios.append(0)
        pre = data
    print(ratios)
    return ratios
            
    

income_pd = pd.read_csv('../data/income.csv',index_col=0)
plt_income(income_pd['000016'].values.tolist(),income_pd['000016'].index.tolist(),'上证50')
plt_income(income_pd['399905'].values.tolist(),income_pd['399905'].index.tolist(),'中证500')
plt_income(income_pd['000932'].values.tolist(),income_pd['000932'].index.tolist(),'中证消费')
plt_income(income_pd['000960'].values.tolist(),income_pd['000960'].index.tolist(),'中证龙头')
plt_income(income_pd['399922'].values.tolist(),income_pd['399922'].index.tolist(),'中证红利')
plt_income(income_pd['399300'].values.tolist(),income_pd['399300'].index.tolist(),'沪深300')
plt_income(income_pd['399006'].values.tolist(),income_pd['399006'].index.tolist(),'创业板')
plt_income(income_pd['399701'].values.tolist(),income_pd['399701'].index.tolist(),'深证F60')
plt_income(income_pd['000978'].values.tolist(),income_pd['000978'].index.tolist(),'医药100')
plt_income(income_pd['399005'].values.tolist(),income_pd['399005'].index.tolist(),'中小板')














