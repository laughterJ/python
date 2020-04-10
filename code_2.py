# Python 中的列表

# 列表中元素可以为不同类型
data = ["String", "int", "double", "bool", 1, 2.8]
print(data)

# 列表支持索引访问，索引从0开始,可以为负数
print(data[0])
# 索引为 -1 时表示最后一个元素，依次类推
print(data[-2])

# 向列表中添加元素
data.append(8.8)
print(data)

# 修改列表中的元素
data[0] = data[0].lower()
print(data)

# 在列表中插入元素
data.insert(1, "&")
print(data)

# 删除列表中的元素
del data[2]
print(data)

# 删除列表末端的元素并取得该元素（相当于栈的弹出）
print(data.pop())
print(data)
# 删除列表中任意位置的元素
print(data.pop(1))
print(data)

# 删除列表中的某个值(只会删除第一次出现的该元素)
data.insert(0, 2.8)
print(data)
data.remove(2.8)
print(data)

# 对列表进行排序，要求列表中元素为相同类型
data = ["String", "bool", "Double", "int"]
data.sort()
print(data)

# sorted() 函数可对列表排序，并返回新的列表，不改变原列表
data = ["String", "bool", "Double", "int"]
print(sorted(data))
print(data)

# 列表倒序
data.reverse()
print(data)

# 列表长度
print(len(data))