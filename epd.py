#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import os
picdir ='weatherIcon'
libdir ='lib'
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in9b_V3
import time
from datetime import datetime
from PIL import Image,ImageDraw,ImageFont
import traceback

class Epd:
    # 获取日期
    def get_date(self):
        today = datetime.today()
        year = today.year
        month = today.month
        day = datetime.now().day
    
        date = f'{year}年{month}月{day}日'
        return date

    # 获取星期
    def get_week(self):
        day_week = datetime.now().weekday()
        if 0 == day_week:
            week = '星期一'
        elif 1 == day_week:
            week = '星期二'
        elif 2 == day_week:
            week = '星期三'
        elif 3 == day_week:
            week = '星期四'
        elif 4 == day_week:
            week = '星期五'
        elif 5 == day_week:
            week = '星期六'
        elif 6 == day_week:
            week = '星期日'
        return week

    # 显示天气信息
    #def display(self, city, weather, temp, aqi, icon):
    def display(self, city, weather, temp, aqi, icon, wind_dir, wind_scale):
        try:
            epd = epd2in9b_V3.EPD()
            epd.init()
            epd.Clear()
            time.sleep(1)
            
            HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
            HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126    
            wimage = Image.open(os.path.join(picdir, icon+'.bmp'))  
            HBlackimage.paste(wimage, (20,20))    
            drawblack = ImageDraw.Draw(HBlackimage)
            text1 = '今日天气'
            mfont = ImageFont.truetype('/usr/share/fonts/truetype/wyq/wqy-microhei.ttc', 15)
            # 绘制提示语
            drawblack.text((20,0), '树莓派智能天气^_^今天又是美好的一天!', font = mfont, fill = 0)
            font = ImageFont.truetype('/usr/share/fonts/truetype/wyq/wqy-microhei.ttc', 18)
            # 画两条横线
            drawblack.line((20, 15, 280, 15), fill=0)
            drawblack.line((20, 105, 280, 105), fill=0)
            # 画两条竖线
            drawblack.line((85, 16, 85, 104), fill=0)
            drawblack.line((228, 16, 228, 104), fill=0)
            # 画四条斜线
            drawblack.line((0, 0, 20, 16), fill=0)
            drawblack.line((297, 0, 280, 16), fill=0)
            drawblack.line((20, 105, 0, 125), fill=0)
            drawblack.line((280, 105, 297, 125), fill=0)

            # 添加城市文字
            drawblack.text((30, 85), city, font = font, fill = 0)
            # 设置字体
            midfont = ImageFont.truetype('/usr/share/fonts/truetype/wyq/wqy-microhei.ttc', 17)
            # 绘制天气文字
            drawblack.text((90, 20), f'{text1}:{weather}', font = midfont, fill = 0)
            # 绘制空气质量文字
            drawblack.text((90, 45), f'空气质量:{aqi}', font = midfont, fill = 0)
            # 绘制风向和风力文字
            drawblack.text((90, 70), f'风力:{wind_dir}{wind_scale}级', font = midfont, fill = 0)
            #drawblack.rectangle((0, 10, 200, 34), fill = 0)
            date = self.get_date()
            # 显示日期
            drawblack.text((60,106), date, font=font, fill=0)
            week = self.get_week()
            # 显示星期几
            drawblack.text((190,106), week, font=font, fill=0)
            # 显示温度
            tfont = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', 22)
            drawblack.text((230, 50), f'{temp}°C', font=tfont, fill=0)
            #drawblack.text((230, 70), '°C', font=tfont, fill=0)
    
            print("正在绘制中...")
            epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
            time.sleep(2)
            epd.sleep()
            #epd.init()
            #epd.Clear()
                
        except IOError as e:
            logging.info(e)
            
        except KeyboardInterrupt:    
            logging.info("ctrl + c:")
            epd2in9b_V3.epdconfig.module_exit()
            exit()
    
if __name__ == '__main__':
    e = Epd()
    e.display(city='沧州', weather='多云', temp=25, aqi='重度污染', icon='100', wind_dir='东北风', wind_scale='4')
