# 字典

# 在 python 中，字典是一系列键值对
data = {"name" : "Allen", "age" : 18, "sex" : "male"}
print(data["name"])

# 添加键值对
data["grade"] = 7
print(data)

# 删除键值对
del data["sex"]
print(data)

# 遍历字典
for key, val in data.items():
	print(key + "\t" + str(val))

# 遍历字典中所有的 键
for key in data.keys():
	print(key)

# 遍历字典中所有的 值
for val in data.values():
	print(val)

# set() 方法可以剔除列表中重复的元素
data = [1,1,2,2,3,3,4,5,6]
print(set(data))