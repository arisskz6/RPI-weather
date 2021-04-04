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




if __name__ == '__main__':
    mail = [
            "<h1 style='color:red'>石家庄3月天气图</h1>",#可以是html语言
            yagmail.inline('draw_3month.png'),# 这样的话,图片会内嵌到正文
            '早日证得涅槃', #可以是普通文本
            ]
    send_mail(mail)
