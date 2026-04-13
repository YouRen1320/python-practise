# 导包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
gdp=pd.read_csv('data/1960-2019全球GDP数据.csv',encoding='gbk')
cn=gdp[gdp['country']=='中国']
us=gdp[gdp['country']=='美国']
jp=gdp[gdp['country']=='日本']

# 画图
plt.plot(cn['year'].astype(int).values,cn['GDP'].values/ 1e12 ,color='red')
plt.plot(us['year'].astype(int).values,us['GDP'].values/ 1e12 ,color='green')
plt.plot(jp['year'].astype(int).values,jp['GDP'].values/ 1e12 ,color='blue')
plt.legend(['中国','美国','日本'])
plt.xlabel('年份')
plt.ylabel('GDP（万亿美元）')
plt.title('中美日GDP变化折线图')
plt.show()