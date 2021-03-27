#测试和风天气API
import requests 
import simplejson as json
import voice
import os
# 获取天气信息
def get_weather():
    #APIURL = "https://devapi.qweather.com/v7/weather/24?"
    APIURL = "https://devapi.qweather.com/v7/weather/now?"
    KEY = "6a6c04efa72d4fb9ae6f0651098e5181"
    LOCATION= '101010200'
    url = APIURL + 'location=' + LOCATION + '&key=' + KEY
    print(url)
    res = requests.get(url)
    final_data = json.loads(res.text) 
    
    test_forecast = final_data['now']['text']
    return test_forecast


if __name__ == '__main__':                                                            
    weather_now = get_weather()
    if weather_now == '晴':
        TEXT = "现在的天气是晴天哦，真棒！"
    voice.main(TEXT) 
    os.system('mpg123 result.mp3') 
