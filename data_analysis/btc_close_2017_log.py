import pygal
import json
import math

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

line_chart = pygal.Line(x_lable_rotation=30, show_minor_x_labels=False)
line_chart.title = "收盘价对数变换（¥）"
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(log_price) for log_price in close_prices]
line_chart.add("log收盘价", close_log)
line_chart.render_to_file("close_price_log.svg")
