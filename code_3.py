# 操作列表

# 遍历列表
data = ["String", "double", "int", "bool"]
for ele in data:
	print(ele)

# range() 函数可以生成一系列整数
for val in range(1,10):
	print(val);
# range() 函数指定步长
for val in range(0,100,8):
	print(val)

# list() 函数 可以将 range() 生成的数字转换成列表
nums = list(range(1,9))
print(nums)

# 对列表进行统计计算
nums = list(range(0,10,3))
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))

# 列表解析
squares = [val ** 2 for val in range(1,11)]
print(squares)

nums = list(range(1,1000001))
print(sum(nums))

nums = [val ** 3 for val in range(1,11)]
print(nums)


# 切片
nums = [val ** 2 for val in range(1,11)]
print(nums[2:5])
print(nums[:5])
print(nums[5:])
# 切片使用的是列表的索引，因此 负数 同样可以使用
print(nums[-8:-5])
print(nums[:-5])
print(nums[-5:])

# 使用切片复制列表
# 切片不指定起始和结束索引，即返回整个列表
nums_1 = nums[:]
# 下面的方式行不通(只是将nums_2这个变量指向nums指向的列表，并不是复制出一个新的列表)
nums_2 = nums