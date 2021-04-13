import requests
from urllib import parse
import simplejson as json
import shelve
import os.path
from os import path
import os
import time

class Voice():

    def __init__(self, text):
        self.text = text

    def get_token(self):
        # 如果存在token.db文件且其中的token未过期，直接从中获取token
        if path.exists('token.db'):
            with shelve.open('token') as db:
                res_dict = db['res_dict']
                empire_time = db['empire_time']
                if  (int(time.time()) + 60) < empire_time:
                    return res_dict['access_token']
        else:
            API_Key = "t4Tce83zz5s5G0Tm4GYLqUW4"            # 官网获取的API_Key
            Secret_Key = "wkfxR2anm4DAb3DDlDU7wUlKGw9NwPVN" # 为官网获取的Secret_Key
            # 拼接请求url
            url = 'https://openapi.baidu.com/oauth/2.0/token?' + 'grant_type=client_credentials' +'&client_id=' + API_Key + '&client_secret=' + Secret_Key
            res = requests.get(url)
            # 将json结果转化为python字典
            res_dict = json.loads(res.text)
            # 持久化返回结果（因为在有效期内token可以重复使用）
            with shelve.open('token') as db:
                db['res_dict'] = res_dict
                # 保存过期时间
                db['empire_time'] = int(time.time()) + res_dict['expires_in']
            return res_dict['access_token']
    
    def text_to_voice(self):
        url = 'http://tsn.baidu.com/text2audio'
        token = self.get_token()
        text = parse.quote_plus(self.text)  # 两次urlencode
        data = {
                    "tex":text, #合成的文本，使用UTF-8编码。小于2048个中文字或者英文数字，文本在百度服务器内转换为GBK后，长度必须小于4096字节（5003、5118发音人需小于512个中文字或者英文数字）
                    "tok":token, #开放平台获取到的开发者access_token
                    "cuid":"e4:5f:01:14:72:15", #用户唯一标识，用来计算UV值。建议填写能区分用户的机器 MAC 地址或 IMEI 码，长度为60字符以内
                    "ctp":1, #客户端类型选择，web端填写固定值1
                    "lan":"zh", #固定值zh。语言选择,目前只有中英文混合模式，填写固定值zh
                    "spd":4, #语速，取值0-15，默认为5中语速
                    "pit":10, #音调，取值0-15，默认为5中语调
                    "vol":10, #音量，取值0-15，默认为5中音量
                    "per":0, #基础语音库，度小宇=1，度小美=0，度逍遥（基础）=3，度丫丫=4
                    "aue":3, #3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav（内容同pcm-16k）
               }
        
        res = requests.post(url=url, data=data)
        if res.headers['Content-Type'] ==  'audio/mp3':
            with open('result.mp3', 'wb') as f:
                f.write(res.content)

    def play(self):
        os.system('mpg123 result.mp3')


#text_to_voice('百度你好')

if __name__ == '__main__':
    v = Voice('百度你好')
    v.text_to_voice()
