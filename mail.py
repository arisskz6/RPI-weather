import yagmail

def send_mail(contents):
    yag = yagmail.SMTP('tianzk404@163.com', 'GDOVEFKHUUZVONUB', host='smtp.163.com', port='465')
    yag.send('3226177006@qq.com', '智能天气小助手', contents)



weather = '晴天'
mail = [
        '主人',
    '今天的天气是', 
    weather
]

if __name__ == '__main__':
    send_mail(mail)
