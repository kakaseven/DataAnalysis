import time
import webbrowser

import numpy as np
import pandas as pd
import pysnowball as ball
import tushare as ts
import browser_cookie3

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 获取xq_a_token
def get_xq_a_token():
    str_xq_a_token = ';'
    while True:
        cj = browser_cookie3.load()
        for item in cj:
            if item.name == "xq_a_token" :
                print('get token, %s = %s' % (item.name, item.value))
                str_xq_a_token = 'xq_a_token=' + item.value + ';'
                return str_xq_a_token
        if str_xq_a_token == ";" :
            print('get token, retrying ......')
            webbrowser.open("https://xueqiu.com/")
            time.sleep(60)

ball.set_token(get_xq_a_token())
pro = ts.pro_api('3fd1861929765ccb35a9a84a5c6ae75d048cb3e5817577c41fba4a9a')

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

data = data[data['list_date'] <= '20170101']
data = data['ts_code'].str.split('.', expand=True)
list = data[1] + data[0]
list.columns = ['stock_code']
stock_data = pd.DataFrame(columns=['code', 'name', 'roe1', 'roe2', 'roe3', 'roe4', 'roe5', 'asset_ratio', 'pe', 'pb', 'dividend_yield', '收益率'])
# log_file = open('log-' + str(time.strftime("-%Y-%m-%d-%H-%M-%S", time.localtime())) + '.txt', 'a+')
for i, stock_code in enumerate(list):
    # print(i, stock_code)
    detail = pd.DataFrame(ball.indicator(symbol=stock_code,is_annals=1,count=5))
    info = pd.DataFrame(ball.quote_detail(stock_code))
    balance = pd.DataFrame(ball.balance(symbol=stock_code,is_annals=1,count=1))
    row1 = detail.loc['list'][0]
    row2 = info.loc['quote'][0]
    row3 = balance.loc['list'][0]
    stock_data.loc[i, 'code'] = stock_code
    stock_data.loc[i, 'name'] = detail.loc['quote_name'][0]
    stock_data.loc[i, 'roe1'] = row1[0]['avg_roe'][0]
    stock_data.loc[i, 'roe2'] = row1[1]['avg_roe'][0]
    stock_data.loc[i, 'roe3'] = row1[2]['avg_roe'][0]
    stock_data.loc[i, 'roe4'] = row1[3]['avg_roe'][0]
    stock_data.loc[i, 'roe5'] = row1[4]['avg_roe'][0]
    stock_data.loc[i, 'asset_ratio'] = row3[0]['asset_liab_ratio'][0]
    stock_data.loc[i, 'pe'] = row2['pe_ttm']
    stock_data.loc[i, 'pb'] = row2['pb']
    stock_data.loc[i, 'dividend_yield'] = row2['dividend_yield']
    stock_data.loc[i, '收益率'] = row2['pb']/row2['pe_ttm']*100 - row2['dividend_yield']*(row2['pb'] - 1)
    print(stock_code)

    
stock_data = stock_data[(stock_data['asset_ratio'] <= 0.5) & (stock_data['roe1'] > 10) & (stock_data['roe2'] > 10) & (stock_data['roe3'] > 10) & (stock_data['roe4'] > 10) & (stock_data['roe5'] > 10)]
stock_data = stock_data.sort_values(by=['收益率'], ascending=False)
stock_data.to_csv('result.csv', encoding='utf_8_sig', index=False)

# print(list.columns)