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
from PIL import Image,ImageDraw,ImageFont
import traceback

class Epd:

    #def display(self, city, weather, temp, aqi, icon, wind_dir, wind_scale):
    def display(self, city, weather, temp, aqi, icon, wind_dir, wind_scale):
        try:
            epd = epd2in9b_V3.EPD()
            epd.init()
            epd.Clear()
            time.sleep(1)
            
        
            HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
            HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126    
            wimage = Image.open(os.path.join(picdir, icon+'.bmp'))  
            HBlackimage.paste(wimage, (20,5))    
            drawblack = ImageDraw.Draw(HBlackimage)
            text1 = '今日天气'
            text2 = f'温度{temp}摄氏度'
            font = ImageFont.truetype('/usr/share/fonts/truetype/wyq/wqy-microhei.ttc', 18)
            drawblack.text((30, 70), city, font = font, fill = 0)
            drawblack.text((120, 20), text1+weather, font = font, fill = 0)
            drawblack.text((120, 45), text2, font = font, fill = 0)
            drawblack.text((120, 70), '空气质量'+aqi, font = font, fill = 0)
            drawblack.text((120, 95), wind_dir+wind_scale+'级', font = font, fill = 0)
            print("正在绘制中...")
            epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
            time.sleep(2)
            epd.sleep()
                
        except IOError as e:
            logging.info(e)
            
        except KeyboardInterrupt:    
            logging.info("ctrl + c:")
            epd2in9b_V3.epdconfig.module_exit()
            exit()
    
if __name__ == '__main__':
    e = Epd()
    e.display(city='沧州', weather='多云', temp=25, aqi='优', icon='100', wind_dir='东北风', wind_scale='4')
