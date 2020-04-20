"""函数"""

# 导入整个模块
import code_8
# 导入特定的函数
from code_8 import print_info_1
# 使用 ad 给模块指定别名
import code_8 as p
# 使用 as 给函数指定别名
from code_8 import print_info_2 as pi
# 导入模块中所有函数
from code_8 import *



# 定义函数
def hello():
	print("Hello python")
# 函数调用
hello()

# 带参函数
def hello(username):
	print("Hello, " + username)

hello("Mr.Jiang")

# 参数列表
def info(name, age, sex):
	print(name + " " + str(age) + " " + sex)

# 位置传参---需要注意参数顺序
info("Jack", 18, "male")
# 关键字传参---顺序无关，只需要准确指定参数名
info(name = "Jack", sex = "male", age = 18)

# 可以为函数参数指定默认值---没有默认值的参数放在前面
def info(name, age, sex, grade = 7):
	print(name + " " + str(age) + " " + sex + " " + str(grade))

info("Jack", 18, "male")

# 函数返回值
def format_name(first_name, last_name):
	full_name = first_name + " " + last_name
	return full_name.title()

print(format_name("Hao", "Jiang"))


# 将函数存储在模块中
code_8.print_info(["name", "age", "sex", "grade"])
print_info_1(["name", "age", "sex", "grade"])
pi(["name", "age", "sex", "grade"])
p.print_info_2(["Jack", 18, "male", 7])
