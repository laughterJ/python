# if语句

age = 10
if age >= 18:
	print("Y")
else:
	print("N")

sex = "female"
if sex == "female":
	print("1")
elif sex == "male":
	print("2")
else:
	print("0")

# python 中用 and 表示 且
if age >= 18 and sex == "female":
	print("Y")
# python 中用 or 表示 或
if age < 18 or sex != "female":
	print("N")


# 检查列表中是否包含指定值
nums = list(range(0,100,3))
num = 30
print(nums)
if num in nums:
	print(str(num) + " in nums")
num = 10
if num not in nums:
	print(str(num) + " not in nums")

