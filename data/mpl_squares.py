import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 指定x、y轴数据及线条宽度
plt.plot(input_values, squares, linewidth=5)
# 设置标题及字体大小
plt.title("Square Numbers", fontsize=24)
# 设置x轴标签及字体大小
plt.xlabel("Value", fontsize=14)
# 设置y轴标签及字体大小
plt.ylabel("Square of Value", fontsize=14)
# axis 设置对哪个轴操作（可选x、y、both），labelsize 设置标记刻度的字号
plt.tick_params(axis="both", labelsize=14)
plt.show()
