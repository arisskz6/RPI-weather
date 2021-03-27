import requests

class Wechat():

    def __init__(self, message):
        self.message = message

    def wechat_send(self):
        res_head = "https://sc.ftqq.com/SCU164119T8b7f9e41cc8534affb101298fcc1af6b6045f039b8111.send?text="
        self.message = res_head + self.message
        requests.get(self.message)


if __name__ == '__main__':
    w = Wechat('测试')
    w.wechat_send()
