# -*- coding: utf-8 -*-
#    Author @tianzhankui
#从和风天气获取天气预报
import requests 
import simplejson as json
import shelve

class Weather:
    KEY = "13e58f9415d04059b86174634fee6adc"
    API_BASE = 'https://devapi.qweather.com/v7/weather/'
    
    def __init__(self, city):
        self.city = city
    
    # 获取城市ID
    def get_location_id(self, adm=None):
        if adm is not None:
            res = requests.get(f'https://geoapi.qweather.com/v2/city/lookup?location={self.city}&key={Weather.KEY}&adm={adm}&range=cn')
        else:
            res = requests.get(f'https://geoapi.qweather.com/v2/city/lookup?location={self.city}&key={Weather.KEY}&range=cn')
        loc_data = json.loads(res.text)
        city_id = loc_data['location'][0]['id']
        return city_id

    # 保存天气数据
    def save_weather_data(self, w_data):
        with shelve.open('data') as db:
            db['w_data'] = w_data

    # 使用天气数据
    def use_weather_data(self):
        with shelve.open('data') as db:
            w_data = db['w_data']
            return w_data
    
    
    # 获取城市天气原始数据
    def get_weather_data(self, time):
        location_id = self.get_location_id()
        if time == 'now':
            API_URL = Weather.API_BASE + 'now?'
        elif time == '24h':
            API_URL = Weather.API_BASE + '24h?'
        elif time == '3d':
            API_URL = Weather.API_BASE + '3d?'
        elif time == '7d':
            API_URL = Weather.API_BASE + '7d?'
        else:
            API_URL = Weather.API_BASE + 'now?'
        url = API_URL + 'location=' + location_id + '&key=' + Weather.KEY
        res = requests.get(url)
        pydic_data = json.loads(res.text) 
        return pydic_data

    # 获取未来指定小时（24小时内）天气预报数据
    def get_future_weather(self, hour=0):
        fu_wdata = self.get_weather_data('24h')
        return fu_wdata['hourly'][hour]

    # 获取空气质量原始数据
    def get_aqi_data_now(self):
        location_id = self.get_location_id()
        url = f'https://devapi.qweather.com/v7/air/now?location={location_id}&key={Weather.KEY}'
        res = requests.get(url)
        pydic_data = json.loads(res.text)
        return pydic_data

    # 获取实时空气质量
    def get_aqi_text_now(self, usedb=False):
        aqi_data = self.get_aqi_data_now()
        return aqi_data['now']['category']
    
    # 获取实时温度
    def get_temp_now(self, usedb=False):
        if usedb is True:
            w_data = self.use_weather_data()
        else:
            w_data = self.get_weather_data('now')
        return w_data['now']['temp']
    
    # 获取实时天气
    def get_weather_text_now(self, usedb=False):
        if usedb is True:
            w_data = self.use_weather_data()
        else:
            w_data = self.get_weather_data('now')
        return w_data['now']['text']
        
    # 获取天气图标代码
    def get_weather_icon(self, usedb=False):
        if usedb is True:
            w_data = self.use_weather_data()
        else:
            w_data = self.get_weather_data('now')
        return w_data['now']['icon']

    # 获取实时风向
    def get_wind_direction_now(self, usedb=False):
        if usedb is True:
            w_data = self.use_weather_data()
        else:
            w_data = self.get_weather_data('now')
        return w_data['now']['windDir']
    
    # 获取实时风力等级
    def get_wind_scale_now(self, usedb=False):
        if usedb is True:
            w_data = self.use_weather_data()
        else:
            w_data = self.get_weather_data('now')
        return w_data['now']['windScale']



if __name__ == '__main__':
    #city = input('请输入您要查询天气的城市: ')
    city = '石家庄'
    w = Weather(city)
    city_id = w.get_location_id()
    print(f'{city} : {city_id}')

    w_data = w.get_weather_data('now')
    # 保存天气数据
    print(w_data)
    #icon = w.get_weather_icon()
    #print('icon:' + icon) 
    #w.save_weather_data(w_data)
    #print('城市: ' + city)
    #print('天气: ' + w.get_weather_text_now(usedb=True))
    #print('温度: ' + w.get_temp_now(usedb=True))
    #print('风向: ' + w.get_wind_direction_now(usedb=True))
    #print('风力: ' + w.get_wind_scale_now(usedb=True) + '级')
    #print('空气质量: ' + w.get_aqi_text_now())

    #w_data = w.get_weather_data('24h')
    #print(w_data)
    #print(w.get_future_weather(hour=3))
    # 测试获取未来3天天气预报信息
    #w_data = w.get_weather_data('3d')
    #print(w_data)
    # 测试逐天获取天气预报信息
    #print(w_data['daily'][0])
    #print(w_data['daily'][1])
    #print(w_data['daily'][2])
