from __future__ import (absolute_import, division, print_function, unicode_literals)
import json
import pygal

filename = "btc_close_2017.json"
with open(filename) as file:
    btc_data = json.load(file)
# 解析 json数据
dates, months, weeks, weekdays, close_prices = [], [], [], [], []
for btc_dict in btc_data:
    dates.append(btc_dict["date"])
    months.append(int(btc_dict["month"]))
    weeks.append(int(btc_dict["week"]))
    weekdays.append(btc_dict["weekday"])
    close_prices.append(int(float(btc_dict["close"])))
# x_label_rotation=20 表示让x轴上的日期标签顺时针旋转20度
# show_minor_x_labels=False 表示不用显示x轴上所有的标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "收盘价（¥）"
line_chart.x_labels = dates
# 设置每隔20天取一次数据
N = 20
line_chart.x_labels_major = dates[::N]
line_chart.add("收盘价", close_prices)
line_chart.render_to_file("close_price.svg")
