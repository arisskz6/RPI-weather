# 根据积累的日天气数据预测未来15天或1个月天气走势
import weather_dev_class as weather
import pandas as pd
import os.path

city = '石家庄'
w = weather.Weather(city)
w_data = w.get_weather_data('3d')
print(w_data)

print(w_data['daily'][0])

dates, weather_text, temp = [], [], []
dates.append(w_data['daily'][0]['fxDate'])
weather_text.append(w_data['daily'][0]['textDay'])
temp.append(w_data['daily'][0]['tempMin'] + ',' +  w_data['daily'][0]['tempMax'])
#print(temp)

# 使用_data表存放日期、天气状况、气温表头及其值
_data = pd.DataFrame()
# 分别将对应值传入 _data 表中
_data['日期'] = dates
_data['天气状况'] = weather_text
_data['气温'] = temp

# 拼接所有表并重新设置行索引（若不进行此步操作，可能或出现多个标签相同的值）
data = pd.concat([_data]).reset_index(drop = True)

# 将 _data 表以 .csv 格式存入指定文件夹中，并设置转码格式防止乱花（注：此转码格式可与 HTML 二进制转字符串的转码格式不同）
if os.path.exists(city +'.csv'):
    data.to_csv(city +'.csv', mode='a', header=False, encoding='utf-8')
else:
    data.to_csv(city + '.csv',encoding='utf-8')
