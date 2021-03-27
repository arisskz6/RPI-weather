# 基于树莓派的智能天气预报系统
import voice
import mail
import weather
import wechat
import os

if __name__ == '__main__':                                                            
    w = weather.Weather()
    weather_now,temp = w.get_weather()
    if weather_now == '晴':
        TEXT = "现在的天气是晴天哦，真棒！"
    if int(temp) < 10:
        TEXT = "当前气温较低，请注意保暖，出门记得穿厚点哦！"
    else:
        TEXT = weather_now
    v = voice.Voice(TEXT) 
    v.textToVoice()
    os.system('mpg123 result.mp3') 
    mail_content = [
            '天气：',
            weather_now,
            '温度：',
            temp,
            ]
    mail.send_mail(mail_content)
