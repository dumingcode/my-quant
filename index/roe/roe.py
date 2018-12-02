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


def plt_income(index_code,index_name,roe_pd,profit_pd,level_pd,turnover_pd,roa_pd):
    roe_arr = roe_pd[index_code].values.tolist()
    bins = roe_pd[index_code].index.tolist()
    income_arr = profit_pd[index_code].values.tolist()
    level_arr = level_pd[index_code].values.tolist()
    turnover_arr = turnover_pd[index_code].values.tolist()
    roa_arr = roa_pd[index_code].values.tolist()
    
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['figure.figsize'] = (24.0, 8.0) # 设置figure_size尺寸
    fig, axes = plt.subplots(3, 2)
    axes[0,0].set_title(index_name+'roe变化')
    axes[0,0].plot(bins,roe_arr, 'o-')
    axes[0,1].set_title(index_name+'净利润率变化')
    axes[0,1].plot(bins,income_arr, 'o-')
    axes[1,0].set_title(index_name+'杠杆变化')
    axes[1,0].plot(bins,level_arr, 'o-')
    axes[1,1].set_title(index_name+'资本周转率变化')
    axes[1,1].plot(bins,turnover_arr, 'o-')
    axes[2,0].set_title(index_name+'roa变化')
    axes[2,0].plot(bins,roa_arr, 'o-')
    
    
    
    
    
    cul = 0
    for a, b in zip(bins, roe_arr):
        cul += 1
        if cul % 4 == 0:
            axes[0,0].text(a, b, float('%.2f' % b), ha='center', va='bottom', fontsize=15)
    cul = 0
    for a, b in zip(bins, income_arr):
        cul += 1
        if cul % 4 == 0:
            axes[0,1].text(a, b, float('%.2f' % b), ha='center', va='bottom', fontsize=15)
    cul = 0
    for a, b in zip(bins, level_arr):
        cul += 1
        if cul % 4 == 0:
            axes[1,0].text(a, b, float('%.2f' % b), ha='center', va='bottom', fontsize=15)
    cul = 0
    for a, b in zip(bins, turnover_arr):
        cul += 1
        if cul % 4 == 0:
            axes[1,1].text(a, b, float('%.2f' % b), ha='center', va='bottom', fontsize=15)
    cul = 0
    for a, b in zip(bins, roa_arr):
        cul += 1
        if cul % 4 == 0:
            axes[2,0].text(a, b, float('%.2f' % b), ha='center', va='bottom', fontsize=15)
    #绘制roe同比变化 净利润 杠杆 周转率贡献比
    cul = 0
    income_compare_year = [0]
    level_compare_year = [0]
    turnovew_compare_year = [0]
    year_arr = []
    min_arr = []
    for a, b in zip(bins, roe_arr):
        cul += 1
        if cul % 4 == 0:
            year_arr.append(bins[cul-1])
        if cul % 4 == 0 and cul >4:    
            if income_arr[cul-5] != 0:
                income_compare_year.append((income_arr[cul-1]-income_arr[cul-5]) / income_arr[cul-5]*100)
            else:
                income_compare_year.append(0)
            if level_arr[cul-5] != 0:
                level_compare_year.append((level_arr[cul-1]-level_arr[cul-5]) / level_arr[cul-5]*100)
            else:
                level_compare_year.append(0)
            if turnover_arr[cul-5] != 0:
                turnovew_compare_year.append(100*(turnover_arr[cul-1]-turnover_arr[cul-5]) / turnover_arr[cul-5])
            else:
                turnovew_compare_year.append(0)
    for i in range(len(income_compare_year)):
        min_arr.append(min(income_compare_year[i],level_compare_year[i],turnovew_compare_year[i]))
    
    
    width = 0.35
    axes[2,1].set_title(index_name+'杜邦公式三要素同比变化率')
    p1=axes[2,1].bar(year_arr, income_compare_year,width)
    p2=axes[2,1].bar(year_arr, level_compare_year,width)
    p3=axes[2,1].bar(year_arr, turnovew_compare_year,width,bottom=min_arr)
    

    plt.legend((p1[0], p2[0], p3[0]), ('净利润', '杠杆','资产周转率'))
    fig.autofmt_xdate()
           
            
    
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

plt_income('000016.XSHG','上证50',roe_pd,profit_pd,level_pd,turnover_pd,roa_pd)
plt_income('000905.XSHG','中证500',roe_pd,profit_pd,level_pd,turnover_pd,roa_pd)
plt_income('000932.XSHG','中证消费',roe_pd,profit_pd,level_pd,turnover_pd,roa_pd)
plt_income('000960.XSHG','中证龙头',roe_pd,profit_pd,level_pd,turnover_pd,roa_pd)
plt_income('000978.XSHG','医药100',roe_pd,profit_pd,level_pd,turnover_pd,roa_pd)
plt_income('399005.XSHE','中小板',roe_pd,profit_pd,level_pd,turnover_pd,roa_pd)
plt_income('000300.XSHG','沪深300',roe_pd,profit_pd,level_pd,turnover_pd,roa_pd)
plt_income('399006.XSHE','创业板',roe_pd,profit_pd,level_pd,turnover_pd,roa_pd)
plt_income('399701.XSHE','深证F60',roe_pd,profit_pd,level_pd,turnover_pd,roa_pd)
plt_income('000922.XSHG','中证红利',roe_pd,profit_pd,level_pd,turnover_pd,roa_pd)

#plt_income(roe_pd['000905.XSHG'].values.tolist(),roe].values.tolist(),turnover_pd['000905.XSHG'].values.tolist(),'中证500')
#plt_income(roe_pd['000932.XSHG'].values.tolist(),roe_pd['000932.XSHG'].index.tolist(),profit_pd['000932.XSHG'].values.tolist(),level_pd['000932.XSHG'].values.tolist(),turnover_pd['000932.XSHG'].values.tolist(),'中证消费')
#plt_income(roe_pd['000960.XSHG'].valu000960.XSHG'].values.tolist(),turnover_pd['000960.XSHG'].values.tolist(),'中证红利')
#plt_income(roe_pd['000978.XSHG'].values.tolist(),roe_pd['000978.XSHG'].index.tolist(),profit_pd['000978.XSHG'].values.tolist(),level_pd['000978.XSHG'].values.tolist(),turnover_pd['000978.XSHG'].values.tolist(),'医药100')

#plt_income(roe_pd['399005.XSHE'].values.tolist(),roe_pd['399005.XSHE'].index.tolist(),profit_pd['399005.XSHE'].values.tolist(),level_pd['399005.XSHE'].values.tolist(),turnover_pd['399005.XSHE'].values.tolist(),'中小板')
#plt_income(roe_pd['000300.XSHG'].values.tolist(),roe_pd['000300.XSHG'].index.tolist(),profit_pd['000300.XSHG'].values.tolist(),level_pd['000300.XSHG'].values.tolist(),turnover_pd['000300.XSHG'].values.tolist(),'沪深300')
#plt_income(roe_pd['399006.XSHE'].values.tolist(),roe_pd['399006.XSHE'].index.tolist(),profit_pd['399006.XSHE'].values.tolist(),level_pd['399006.XSHE'].values.tolist(),turnover_pd['399006.XSHE'].values.tolist(),'创业板')
#plt_income(roe_pd['399701.XSHE'].values.tolist(),roe_pd['399701.XSHE'].index.tolist(),profit_pd['399701.XSHE'].values.tolist(),level_pd['399701.XSHE'].values.tolist(),turnover_pd['399701.XSHE'].values.tolist(),'深证F60')












