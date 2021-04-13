# 基于树莓派的智能天气预报系统
import voice_test as voice
import mail
import weather_dev_class as weather
import wechat_test as wechat
import os
import epd
import history
import predict

if __name__ == '__main__':                                                            
    city = '石家庄'
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
    v.text_to_voice()
    print(weather_now)
    v.play()
    we = wechat.Wechat(TEXT)
    print('正在推送微信消息...')
    we.send()
    print('微信消息推送完毕！')
    print('正在发送天气信息到邮件...')
    mail_content = [
            '天气：',
            weather_now,
            '温度：',
            temp,
            ]
    m = mail.Mail(mail_content)
    m.send()
    print('邮件发送完毕！')
    print('正在启动电子墨水屏显示...')
    e = epd.Epd()
    e.display(city=city, weather=weather_now, temp=temp, aqi=aqi, icon=icon)
    print('电子墨水屏显示完毕！')
    # 获取历史天气数据
    print('正在获取历史天气数据...')
    h = history.History(city)
    h.get_data()
    print('历史天气数据获取完毕！')

    # 预测未来天气
    print('开始预测未来天气...')
    p = predict.Predict(city)
    p.predict()
