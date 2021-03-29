# 基于树莓派的智能天气预报系统
import voice
import mail
import weather_dev_class as weather
import wechat
import os
import epd

if __name__ == '__main__':                                                            
    city = '西双版纳'
    w = weather.Weather(city)
    weather_now = w.get_weather_text_now()
    temp = w.get_temp_now()
    aqi = w.get_aqi_text_now()
    icon = w.get_weather_icon()
    if weather_now == '晴':
        TEXT = "现在的天气是晴天哦，真棒！"
    if int(temp) < 10:
        TEXT = "当前气温较低，请注意保暖，出门记得穿厚点哦！"
    else:
        TEXT = "今天" + city + "天气" + weather_now + "，气温" + temp + "摄氏度" + "，空气质量" + aqi

    v = voice.Voice(TEXT) 
    v.textToVoice()
    print(weather_now)
    os.system('mpg123 result.mp3') 
    we = wechat.Wechat(TEXT)
    we.wechat_send()
    mail_content = [
            '天气：',
            weather_now,
            '温度：',
            temp,
            ]
    mail.send_mail(mail_content)
    e = epd.Epd()
    e.display(city=city, weather=weather_now, temp=temp, aqi=aqi, icon=icon)
