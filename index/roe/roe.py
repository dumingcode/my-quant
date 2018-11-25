# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
展示各个指数roe变化情况
@author duming
"""


    
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

font = {'family': 'Times New Roman',
        'color':  'red',
        'weight': 'normal',
        'size': 15
        }


def plt_income(arr,bins,arr2,bins2,arr3,bins3,arr4,bins4,index_name):
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['figure.figsize'] = (24.0, 8.0) # 设置figure_size尺寸
    fig, axes = plt.subplots(2, 2)
    axes[0,0].set_title(index_name+'roe变化')
    axes[0,0].plot(bins,arr, 'o-')
    axes[0,1].set_title(index_name+'净利润率变化')
    axes[0,1].plot(bins2,arr2, 'o-')
    axes[1,0].set_title(index_name+'杠杆变化')
    axes[1,0].plot(bins3,arr3, 'o-')
    axes[1,1].set_title(index_name+'资本周转率变化')
    axes[1,1].plot(bins4,arr4, 'o-')
    fig.autofmt_xdate()
    cul = 0
    for a, b in zip(bins, arr):
        cul += 1
        if cul % 4 == 0:
            axes[0,0].text(a, b, float('%.2f' % b), ha='center', va='bottom', fontsize=15)
    for a, b in zip(bins2, arr2):
        cul += 1
        if cul % 4 == 0:
            axes[0,1].text(a, b, float('%.2f' % b), ha='center', va='bottom', fontsize=15)
    for a, b in zip(bins3, arr3):
        cul += 1
        if cul % 4 == 0:
            axes[1,0].text(a, b, float('%.2f' % b), ha='center', va='bottom', fontsize=15)
    for a, b in zip(bins4, arr4):
        cul += 1
        if cul % 4 == 0:
            axes[1,1].text(a, b, float('%.2f' % b), ha='center', va='bottom', fontsize=15)
    plt.savefig('../../pic/index_roe/'+index_name, dpi=400) #指定分辨率
    plt.show()


            
# 当年的roe累加 举例子q4为4季度roe之和
def year_roe_cul(roe_pd):
    for row in range(1,roe_pd.shape[0]):
        if row % 4 == 0:      
            pass
        else:
            roe_pd.iloc[row] = roe_pd.iloc[row] + roe_pd.iloc[row-1]
    return roe_pd
    
    

income_pd = pd.read_csv('../../data/index_roe/index_roe.csv',index_col=0)
roe_pd = year_roe_cul(income_pd)
profit_pd = pd.read_csv('../../data/index_roe/index_net_profit_margin.csv',index_col=0)
level_pd = pd.read_csv('../../data/index_roe/index_level.csv',index_col=0)
roa_pd = pd.read_csv('../../data/index_roe/index_roa.csv',index_col=0)

turnover_pd = roa_pd/profit_pd*100
turnover_pd = turnover_pd.fillna(0)

plt_income(roe_pd['000016.XSHG'].values.tolist(),roe_pd['000016.XSHG'].index.tolist(),profit_pd['000016.XSHG'].values.tolist(),profit_pd['000016.XSHG'].index.tolist(),level_pd['000016.XSHG'].values.tolist(),level_pd['000016.XSHG'].index.tolist(),turnover_pd['000016.XSHG'].values.tolist(),turnover_pd['000016.XSHG'].index.tolist(),'上证50')
plt_income(roe_pd['000905.XSHG'].values.tolist(),roe_pd['000905.XSHG'].index.tolist(),profit_pd['000905.XSHG'].values.tolist(),profit_pd['000905.XSHG'].index.tolist(),level_pd['000905.XSHG'].values.tolist(),level_pd['000905.XSHG'].index.tolist(),turnover_pd['000905.XSHG'].values.tolist(),turnover_pd['000905.XSHG'].index.tolist(),'中证500')
plt_income(roe_pd['000932.XSHG'].values.tolist(),roe_pd['000932.XSHG'].index.tolist(),profit_pd['000932.XSHG'].values.tolist(),profit_pd['000932.XSHG'].index.tolist(),level_pd['000932.XSHG'].values.tolist(),level_pd['000932.XSHG'].index.tolist(),turnover_pd['000932.XSHG'].values.tolist(),turnover_pd['000932.XSHG'].index.tolist(),'中证消费')
plt_income(roe_pd['000960.XSHG'].values.tolist(),roe_pd['000960.XSHG'].index.tolist(),profit_pd['000960.XSHG'].values.tolist(),profit_pd['000960.XSHG'].index.tolist(),level_pd['000960.XSHG'].values.tolist(),level_pd['000960.XSHG'].index.tolist(),turnover_pd['000960.XSHG'].values.tolist(),turnover_pd['000960.XSHG'].index.tolist(),'中证红利')
plt_income(roe_pd['000978.XSHG'].values.tolist(),roe_pd['000978.XSHG'].index.tolist(),profit_pd['000978.XSHG'].values.tolist(),profit_pd['000978.XSHG'].index.tolist(),level_pd['000978.XSHG'].values.tolist(),level_pd['000978.XSHG'].index.tolist(),turnover_pd['000978.XSHG'].values.tolist(),turnover_pd['000978.XSHG'].index.tolist(),'医药100')

plt_income(roe_pd['399005.XSHE'].values.tolist(),roe_pd['399005.XSHE'].index.tolist(),profit_pd['399005.XSHE'].values.tolist(),profit_pd['399005.XSHE'].index.tolist(),level_pd['399005.XSHE'].values.tolist(),level_pd['399005.XSHE'].index.tolist(),turnover_pd['399005.XSHE'].values.tolist(),turnover_pd['399005.XSHE'].index.tolist(),'中小板')
plt_income(roe_pd['000960.XSHG'].values.tolist(),roe_pd['000960.XSHG'].index.tolist(),profit_pd['000960.XSHG'].values.tolist(),profit_pd['000960.XSHG'].index.tolist(),level_pd['000960.XSHG'].values.tolist(),level_pd['000960.XSHG'].index.tolist(),turnover_pd['000960.XSHG'].values.tolist(),turnover_pd['000960.XSHG'].index.tolist(),'中证龙头')
plt_income(roe_pd['000300.XSHG'].values.tolist(),roe_pd['000300.XSHG'].index.tolist(),profit_pd['000300.XSHG'].values.tolist(),profit_pd['000300.XSHG'].index.tolist(),level_pd['000300.XSHG'].values.tolist(),level_pd['000300.XSHG'].index.tolist(),turnover_pd['000300.XSHG'].values.tolist(),turnover_pd['000300.XSHG'].index.tolist(),'沪深300')
plt_income(roe_pd['399006.XSHE'].values.tolist(),roe_pd['399006.XSHE'].index.tolist(),profit_pd['399006.XSHE'].values.tolist(),profit_pd['399006.XSHE'].index.tolist(),level_pd['399006.XSHE'].values.tolist(),level_pd['399006.XSHE'].index.tolist(),turnover_pd['399006.XSHE'].values.tolist(),turnover_pd['399006.XSHE'].index.tolist(),'创业板')
plt_income(roe_pd['399701.XSHE'].values.tolist(),roe_pd['399701.XSHE'].index.tolist(),profit_pd['399701.XSHE'].values.tolist(),profit_pd['399701.XSHE'].index.tolist(),level_pd['399701.XSHE'].values.tolist(),level_pd['399701.XSHE'].index.tolist(),turnover_pd['399701.XSHE'].values.tolist(),turnover_pd['399701.XSHE'].index.tolist(),'深证F60')












