# 数据可视化
from matplotlib import pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 第一步：数据读取
data = pd.read_csv('Shijiazhuang4Mouth.csv')
# 第二步：数据处理（由于我们知道文本内容，不存在脏数据，故忽略数据清理步骤）
data['最高气温'] = data['气温'].str.split('/',expand=True)[0]
data['最低气温'] = data['气温'].str.split('/',expand=True)[1]

data['最高气温'] = data['最高气温'].map(lambda x:x.replace('℃,',''))
data['最低气温'] = data['最低气温'].map(lambda x:x.replace(',',''))
data['最低气温'] = data['最低气温'].map(lambda x:x.replace('℃',''))
data['最高气温'] = data['最高气温'].astype("int")
data['最低气温'] = data['最低气温'].astype("int")
print(data['最高气温'])

dates = data['日期']
highs = data['最高气温']
lows = data['最低气温']

# 画图（折线图）
# 设置画布大小及比例
fig = plt.figure(dpi=128,figsize=(10,6))

# 设置最高温最低温线条颜色及宽度等信息
L1,=plt.plot(dates,lows,label='最低气温')
L2,=plt.plot(dates,highs,label='最高气温')
plt.legend(handles=[L1,L2],labels=['最高气温','最低气温'], loc='best')# 添加图例

# 图表格式
# 设置图形格式
plt.title('2021年4月石家庄天气',fontsize=25)  # 字体大小设置为25
plt.xlabel('日期',fontsize=10)   # x轴显示“日期”，字体大小设置为10
fig.autofmt_xdate() # 绘制斜的日期标签，避免重叠
plt.ylabel('气温',fontsize=10)  # y轴显示“气温”，字体大小设置为10
plt.tick_params(axis='both',which='major',labelsize=10)

# 修改刻度
plt.xticks(dates[::1])  # 由于数据不多，将每天的数据全部显示出来

# 显示折线图
plt.show()
# 保存折线图
plt.savefig('draw_3month.png')
