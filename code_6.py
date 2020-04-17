# 用户输入和while循环

# input() 函数可以获取用户输入
# msg = input("Hello")
# print(msg)


# input() 函数读取用户输入时默认为string，需要时可进行类型转换
# age = input("age : ")
# age = int(age)

# 求模运算符
num = 10 % 3
print(num)

# while 循环
cur_num = 1;
while cur_num <= 20:
	print(cur_num)
	cur_num += 3

# 使用 break 退出循环
num = 1
while True:
	if num % 10 == 8:
		print(str(num) + "\tover")
		break
	else:
		num += 1

# 使用 continue 跳出本次循环，继续执行下一次循环
num = 0
while num < 10:
	num += 1
	if num % 2 == 0:
		continue
	print(num)

# 使用 while 循环来处理列表和字典
data_list = ["Allen", "Pany", "Mike"]
empty_list = []
while data_list:
	empty_list.append(data_list.pop())
print(data_list)
print(empty_list)

num = 1
num_list = [1, 1, 2, 1, 3, 5, 4, 1]
while num in num_list:
	print(num_list)
	num_list.remove(num)
	print(num_list)