import requests
import json

class Wechat():
    def __init__(self, contents):
        self.contents = contents

    def send(self):
        wxpush_url = 'http://wxpusher.zjiecode.com/api/send/message'
        data = {
                    "appToken":"AT_fIZVgg4T6oGclt3SgloPTGYKH2k2clWX",
                    "content":self.contents,
                    "contentType":1,
                    "uids":[
                            "UID_rDVj3psx8ufLKqzUVQt4LLrfnvUM"
                            ],   
               }
        
        ## headers中添加上content-type这个参数，指定为json格式
        headers = {'Content-Type': 'application/json'}
         
        ## post的时候，将data字典形式的参数用json包转换成json格式。
        res = requests.post(url=wxpush_url, headers=headers, data=json.dumps(data))
        res_dict = json.loads(res.text)
        #print(res_dict['success'])


if __name__ == '__main__':
    msg = input('请输入您要发送到微信的消息文本：')
    w = Wechat(msg)
    w.send()
