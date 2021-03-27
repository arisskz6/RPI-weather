#从和风天气获取天气预报
import requests 
import simplejson as json
class Weather():
    def __init__(self, location='101010200'):
        self.location = location

    def get_weather(self):
        APIURL = "https://devapi.qweather.com/v7/weather/24h?"
        #APIURL = "https://devapi.qweather.com/v7/weather/now?"
        KEY = "cd333976c10a4316b0a9d3d8735a2f74"
        LOCATION = self.location
        url = APIURL + 'location=' + LOCATION + '&key=' + KEY
        print(url)
        res = requests.get(url)
        final_data = json.loads(res.text) 
        
#        test_forecast = final_data['now']['text']
#        tmp = final_data['now']['temp']
    
#        return test_forecast, tmp
        return final_data

if __name__ == '__main__':
    w = Weather()
    w_data = w.get_weather()
    print(w_data['hourly'][0]['temp'])
