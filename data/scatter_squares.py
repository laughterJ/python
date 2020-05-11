import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [val**2 for val in x_values]
x_values = list(range(0, 1001))
y_values = [val ** 2 for val in x_values]
# c 设置数据点颜色，edgecolors 设置数据点轮廓颜色
# plt.scatter(x_values, y_values, c="red", edgecolors="none", s=10)
# 使用颜色映射(将参数c设置为y值列表，并指定camp参数使用红色作颜色映射)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors="none", s=10)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# which 设置对主、副坐标轴进行操作（可选 major、minor、both)
plt.tick_params(axis="both", which="major", labelsize=14)
# 设置坐标轴取值范围依次为[xmin, xmax, ymin, ymax]
plt.axis([0, 1100, 0, 1100000])
# plt.show()
# 将图表保存为图片
plt.savefig("squares_plot.png", bbox_inches="tight")
