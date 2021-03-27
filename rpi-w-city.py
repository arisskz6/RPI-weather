# 测试和风天气API
import requests 
import simplejson as json
APIURL = "https://geoapi.qweather.com/v2/city/lookup"
CITY = "beijing"
KEY = "6a6c04efa72d4fb9ae6f0651098e5181"
url = APIURL + '?location=' + CITY + '&key=' + KEY
res = requests.get(url)
final_data = json.loads(res.text) 

forecast = final_data['HeWeather6'][0]['daily_forecast']
for data in forecast:
    cond_txt_d = data['cond_txt_d']  # weather 天气描述
    tmp_max = data['tmp_max']  # max temperature.
    tmp_min = data['tmp_min']  # min tempereture.
    hum = data['hum']  # humanity
    wind_dir = data['wind_dir']  # wind direction.
    wind_sc = data['wind_sc']  # wind degree.
    wind_spd = data['wind_spd']  # wind speed.
print(cond_text_d)
print(tmp_max)
print(tmp_min)
print(hum)
print(wind_dir)
print(wind_sc)
print(wind_spd)
