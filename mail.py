import yagmail

class Mail():
    def __init__(self, contents):
        self.contents = contents

    def send(self):
        sender = 'tianzk404@163.com'
        reciver = ['3226177006@qq.com', 'tianzk404@163.com']
        password = 'GDOVEFKHUUZVONUB'
        host = 'smtp.163.com'
        port = '465'
    
        yag = yagmail.SMTP(sender, password, host, port)
        subject = 'arisskz6'
        yag.send(reciver, subject, self.contents)




if __name__ == '__main__':
    mail = [
            "树莓派智能天气提醒",
            ]
    m = Mail(mail)
    m.send()
    print("发送成功")
