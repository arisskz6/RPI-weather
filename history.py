import requests
from bs4 import BeautifulSoup
import shelve
import os.path
from os import path
import pandas as pd
import datetime
from pypinyin import pinyin, Style

class History():

    def __init__(self, city):
        self.city = city


    def chinese_to_pinyin(self, text):
        rs = pinyin(text, style=Style.NORMAL)
        f_str = ''
        for e in rs:
            f_str = f_str + e[0]
        return f_str
    
    def get_data(self):
        city = self.chinese_to_pinyin(self.city)
        today = datetime.datetime.today()
        uri = str(today.year) + str(today.month).zfill(2)
        day = datetime.datetime.now().day
        dbfile_pre = city + uri + str(day)
    
        if path.exists(dbfile_pre + '.db'):
            with shelve.open(dbfile_pre) as db:
                html = db['html']
        else:
            url = f'http://www.tianqihoubao.com/lishi/{city}/month/{uri}.html'
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                html = res.text
                # 数据持久化
                with shelve.open(dbfile_pre) as db:
                    db['html'] = html
            else:
                print("Error, please check your network connection.")
        soup = BeautifulSoup(html, 'lxml')
        trs = soup.find_all('tr')
        dates, weathers, temps = [], [], []
        
        for tr in trs:
            tds = tr.find_all('td')
            td_list = []
            # 获取除风力风向外的所有元素
            for td in tds[:-1]:
                td_list.append(td.text.strip().replace('\r\n', '').replace(' ', ''))
        
            if td_list[0] != '日期':
                dates.append(td_list[0])
                weathers.append(td_list[1])
                temps.append(td_list[2])
        
        # 使用 data 表存放日期、天气状况、气温表头及其值
        data = pd.DataFrame()
        data['日期'] = dates
        data['天气状况'] = weathers
        data['气温'] = temps
        # 拼接所有表并重新设置行索引（若不进行此步操作，可能或出现多个标签相同的值）
        data = pd.concat([data]).reset_index(drop = True)
        # 将 data 表以 .csv 格式存储，并设置转码格式防止乱码
        data.to_csv(city + uri + '.csv',encoding='utf-8')


if __name__ == '__main__':
    p = History("石家庄")
    p.get_data()
