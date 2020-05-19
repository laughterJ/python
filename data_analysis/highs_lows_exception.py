import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "death_valley_2014.csv"
# 打开文件，并将文件对象存储在file中
with open(filename) as file:
    # 创建一个与文件相关联的阅读器
    reader = csv.reader(file)
    # 读取文件第一行
    header_row = next(reader)

    # enumerate()函数用于将一个可遍历的数据对象组合为一个索引序列
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # 使用for循环依次遍历文件每一行，并且取其第一列生成列表
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print("missing data")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red", linewidth=0.5)
plt.plot(dates, lows, c="blue", linewidth=0.5)
plt.fill_between(dates, lows, highs, facecolor="black", alpha=0.2)
plt.title("Daily low and high temperatures - 2014\nDeath Valley, CA", fontsize=24)
plt.xlabel("day", fontsize=16)
# 将x轴标签即日期倾斜绘制，避免重叠
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.show()
