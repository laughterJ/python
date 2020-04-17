"""函数"""

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


