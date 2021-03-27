#从和风天气获取天气预报
import requests 
import simplejson as json

KEY = "cd333976c10a4316b0a9d3d8735a2f74"
API_BASE = 'https://devapi.qweather.com/v7/weather/'


# 获取城市ID
def get_city_id(city='石家庄', adm=None):
    if adm is not None:
        res = requests.get(f'https://geoapi.qweather.com/v2/city/lookup?location={city}&key=6a6c04efa72d4fb9ae6f0651098e5181&adm={adm}&range=cn')
    else:
        res = requests.get(f'https://geoapi.qweather.com/v2/city/lookup?location={city}&key=6a6c04efa72d4fb9ae6f0651098e5181&range=cn')
    loc_data = json.loads(res.text)
    city_id = loc_data['location'][0]['id']
    return city_id


# 获取城市天气原始数据
def get_weather_data(location_id, time):
    if time == 'now':
        API_URL = API_BASE + 'now?'
    elif time == '24h':
        API_URL = API_BASE + '24h?'
    else:
        API_URL = API_BASE + 'now'
    url = API_URL + 'location=' + location_id + '&key=' + KEY
    res = requests.get(url)
    final_data = json.loads(res.text) 
    return final_data

# 获取实时温度
def get_temp_now(location_id):
    w_data = use_weather_data()
    return w_data['now']['temp']

# 获取实时天气
def get_weather_text_now(location_id):
    w_data = get_weather_data(location_id, 'now')
    return w_data['now']['text']
    
# 获取实时风向
def get_wind_direction_now(location_id):
    w_data = get_weather_data(location_id, 'now')
    return w_data['now']['windDir']

# 获取实时风力等级
def get_wind_scale_now(location_id):
    w_data = get_weather_data(location_id, 'now')
    return w_data['now']['windScale']

if __name__ == '__main__':
    city = input('请输入您要查询天气的城市: ')
    location_id = get_city_id(city)
    w_data = get_weather_data(location_id, 'now')

    print('city: ' + city)
    print('temp: ' + get_temp_now())
    print('weather: ' + get_weather_text_now())
