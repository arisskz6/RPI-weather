import yagmail

def send_mail(contents):
    sender = 'tianzk404@163.com'
    reciver = '3226177006@qq.com'
    password = 'GDOVEFKHUUZVONUB'
    host = 'smtp.163.com'
    port = '465'

    yag = yagmail.SMTP(sender, password, host, port)
    subject = '树莓派智能天气提醒'
    yag.send(reciver, subject, contents)



weather = '晴天'
mail = [
        '主人',
    '今天的天气是', 
    weather
]

if __name__ == '__main__':
    send_mail(mail)
