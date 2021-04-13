import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
import history
import logging
logging.getLogger('matplotlib.font_manager').disabled = True

class Predict():
    def __init__(self, city):
        self.city = city

    def predict(self):
        city=self.city
        today = datetime.datetime.today()
        uri = str(today.year) + str(today.month).zfill(2)
        day = datetime.datetime.now().day
        h = history.History(city)
        # 将中文城市名称转换成拼音
        city_name = h.chinese_to_pinyin(city)
        csv_file = city_name + uri + '.csv'
        # 从csv文件中读取历史天气数据
        data = pd.read_csv(csv_file)
        # 由于最高气温与最低气温中有 / 分隔，故将其分开，即“气温”列由一列变为两列——“最高气温”和“最低气温”
        data['最高气温'] = data['气温'].str.split('/',expand=True)[0]
        # 将多余的单位 ℃ 从列表中去掉，只保留数值部分
        data['最高气温'] = data['最高气温'].map(lambda x:x.replace('℃',''))
        # 日次操作同理
        data['日期'] = data['日期'].map(lambda x:x.replace(str(today.year) + '年' + str(today.month).zfill(2) +'月0',''))
        data['日期'] = data['日期'].map(lambda x:x.replace('日',''))
        data['日期'] = data['日期'].map(lambda x:x.replace(str(today.year) + '年' + str(today.month).zfill(2) + '月',''))
        data['日期'] = data['日期'].astype("int")
        data['最高气温'] = data['最高气温'].astype("int")
        
        
        # 传入对应日期及其最高气温参数
        # 应以矩阵形式表达(对于单变量，矩阵就是列向量形式)
        xTrain = np.array(data['日期'])[:, np.newaxis]
        # 为方便理解，也转换成列向量
        yTrain = np.array(data['最高气温'])
        
        # 创建模型对象
        model = LinearRegression()
        # 根据训练数据拟合出直线(以得到假设函数)
        hypothesis = model.fit(xTrain, yTrain)
        # 截距
        #print("theta0=", hypothesis.intercept_)
        # 斜率
        #print("theta1=", hypothesis.coef_)
        
        # 预测明天最高气温
        next_day = day + 1
        print(f"预测{today.year}年{today.month}月{next_day}日的最高气温：", model.predict([[next_day]]))
        # 也可以批量预测多个日期的气温，注意要以列向量形式表达（有余数据集量少，故间隔时间长气温可能有较大差异）
        # 此处仅利用模型表示，不代表真实值（假设要预测未来三天的天气）
        day1 = day + 1
        day2 = day + 2
        day3 = day + 3
        xNew = np.array([0, day1, day2, day3])[:, np.newaxis]
        yNew = model.predict(xNew)
        print("预测新数据：", xNew)
        print("预测结果：", yNew)

        # 绘制预测图
        # 先准备好一块画布
        plt.figure()
        # 生成图表的名字
        title = f'{today.year}年{today.month}月迄今{city}天气'
        plt.title(title)
        # 横坐标名字
        plt.xlabel('日期')
        # 纵坐标名字
        plt.ylabel('当日最高气温')
        # 表内有栅格
        plt.grid(True)
        # k是黑色，.是以点作为图上显示
        plt.plot(xTrain, yTrain, 'k.')
        # 画出通过这些点的连续直线
        plt.plot(xNew, yNew, 'g--')
        # 保存图片
        plt.savefig('predict.png', dpi=199)


if __name__ == '__main__':
    city = '石家庄'
    p = Predict(city)
    p.predict()
