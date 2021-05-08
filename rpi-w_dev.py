# 基于树莓派的智能天气预报系统
import ping
import voice
import yagmail
import mail
import weather
import wechat
import os
import epd
import history
import predict
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def rpi_weather():
    if ping.check_network() is True:
        city = '石家庄'
        w = weather.Weather(city)
        weather_now = w.get_weather_text_now()
        temp = w.get_temp_now()
        aqi = w.get_aqi_text_now()
        icon = w.get_weather_icon()
        wind_dir = w.get_wind_direction_now()
        wind_scale = w.get_wind_scale_now()
    
        if weather_now == '晴':
            TEXT = "现在的天气是晴天哦，真棒！"
        if int(temp) < 10:
            TEXT = "当前气温较低，请注意保暖，出门记得穿厚点哦！"
        else:
            TEXT = f'树莓派智能天气提醒您：今天{city}天气{weather_now}，气温{temp}摄氏度，空气质量{aqi}，{wind_dir}{wind_scale}级'
    
        v = voice.Voice(TEXT) 
        v.text_to_voice()
        print('正在进行语音播报...')
        v.play(flag=True)
        print('语音播报完毕！')
        we = wechat.Wechat(TEXT)
        print('正在推送微信消息...')
        we.send()
        print('微信消息推送完毕！')
        print('正在启动电子墨水屏显示...')
        e = epd.Epd()
        e.display(city=city, weather=weather_now, temp=temp, aqi=aqi, icon=icon, wind_dir=wind_dir, wind_scale=wind_scale)
        print('电子墨水屏显示完毕！')
        # 获取历史天气数据
        print('正在获取历史天气数据...')
        h = history.History(city)
        h.get_data()
        print('历史天气数据获取完毕！')
    
        # 预测未来天气
        print('开始预测未来天气...')
        p = predict.Predict(city)
        xNew, yNew = p.predict()
        print('正在发送天气信息到邮件...')
        mail_content = [
                f'<h1 style="color:red">树莓派智能天气提醒</h1>',
                f'{city}今日天气：{weather_now}',
                f'气温：{temp}摄氏度', 
                f'空气质量：{aqi}',
                f'风力：{wind_dir}{wind_scale}级',
                f'预测新数据：{xNew}',
                f'预测结果：{yNew}',
                '<p style="color:green"><strong>未来气温预测图: </strong></p>',
                yagmail.inline('predict.png'), 
                ]
        m = mail.Mail(mail_content)
        m.send()
        print('邮件发送完毕！')
    else:
        TEXT = "对不起，网络连接异常，请检查! 对不起，网络连接异常，请检查！对不起，网络连接异常，请检查！"
        v = voice.Voice(TEXT)
        v.play(flag=False)
    

# 创建定时任务
def timer_job():
     rpi_weather()
     # BlockingScheduler
     scheduler = BlockingScheduler()
     scheduler.add_job(timer_job, 'cron', day_of_week='1-5', hour=7, minute=30)
     scheduler.start()

if __name__ == "__main__":
    #timer_job()
    rpi_weather()
