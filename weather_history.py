import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(url):
    # 请求网页（第三方 requests）
    resp = requests.get(url)
    # 对于获取到的 HTML 二进制文件进行 'gbk' 转码成字符串文件
    html = resp.content.decode('gbk')
    # 通过第三方库 BeautifulSoup 缩小查找范围（同样作用的包库还有re模块、xpath等）
    soup = BeautifulSoup(html,'html.parser')
    # 获取 HTML 中所有<tr>…</tr>标签，因为我们需要的数据全部在此标签中存放
    tr_list = soup.find_all('tr')
    # 初始化日期dates、气候contains、温度temp值
    dates,contains,temp = [],[],[]
    for data in tr_list[1:]:  # 不要表头
        # 数据值拆分，方便进一步处理（这里可以将获得的列表输出[已注释]，不理解的读者可运行查看)
        sub_data = data.text.split()
        # print(sub_data)
        # 观察上一步获得的列表，这里只想要获得列表中第二个和第三个值，采用切片法获取
        dates.append(sub_data[0])
        contains.append(','.join(sub_data[1:3]))
        # print(contains)
        # 同理采用切片方式获取列表中的最高、最低气温
        temp.append(','.join(sub_data[3:6]))
        # print(temp)
    # 使用 _data 表存放日期、天气状况、气温表头及其值
    _data = pd.DataFrame()
    # 分别将对应值传入 _data 表中
    _data['日期'] = dates
    _data['天气状况'] = contains
    _data['气温'] = temp
    return _data

# 爬取目标网页（石家庄市2021年3月份天气[网站：天气后报]）
data_2_month = get_data('http://www.tianqihoubao.com/lishi/shijiazhuang/month/202103.html')

# 拼接所有表并重新设置行索引（若不进行此步操作，可能或出现多个标签相同的值）
data = pd.concat([data_2_month]).reset_index(drop = True)

# 将 _data 表以 .csv 格式存入指定文件夹中，并设置转码格式防止乱花（注：此转码格式可与 HTML 二进制转字符串的转码格式不同）
data.to_csv('Shijiazhuang3Mouth.csv',encoding='utf-8')
