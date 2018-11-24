# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
展示各个指数roe变化情况
@author duming
"""


    
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

def plt_income(arr,bins,index_name):
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['figure.figsize'] = (16.0, 4.0) # 设置figure_size尺寸
    fig, (ax0) = plt.subplots(ncols=1)
    ax0.set_title(index_name+'roe变化')
    ax0.plot(bins,arr, 'o-')
    fig.autofmt_xdate()
    plt.savefig('../../pic/index_roe/'+index_name, dpi=200) #指定分辨率
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
plt_income(roe_pd['000016.XSHG'].values.tolist(),roe_pd['000016.XSHG'].index.tolist(),'上证50')
plt_income(roe_pd['000905.XSHG'].values.tolist(),roe_pd['000905.XSHG'].index.tolist(),'中证500')
plt_income(roe_pd['000932.XSHG'].values.tolist(),roe_pd['000932.XSHG'].index.tolist(),'中证消费')
plt_income(roe_pd['000960.XSHG'].values.tolist(),roe_pd['000960.XSHG'].index.tolist(),'中证龙头')
plt_income(roe_pd['000922.XSHG'].values.tolist(),roe_pd['000922.XSHG'].index.tolist(),'中证红利')
plt_income(roe_pd['000300.XSHG'].values.tolist(),roe_pd['000300.XSHG'].index.tolist(),'沪深300')
plt_income(roe_pd['399006.XSHE'].values.tolist(),roe_pd['399006.XSHE'].index.tolist(),'创业板')
plt_income(roe_pd['399701.XSHE'].values.tolist(),roe_pd['399701.XSHE'].index.tolist(),'深证F60')
plt_income(roe_pd['000978.XSHG'].values.tolist(),roe_pd['000978.XSHG'].index.tolist(),'医药100')
plt_income(roe_pd['399005.XSHE'].values.tolist(),roe_pd['399005.XSHE'].index.tolist(),'中小板')














