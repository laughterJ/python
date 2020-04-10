print("hello python")
print("hello world")


# 变量的命名
# 变量名只能包含字母、数字、下划线，不能以数字开头
# 变量名不能包含空格
# 不能将 python 关键字和函数名用作变量名
# 避免使用大写字母

msg = "You never know how strong you are until being strong is the only choice you have."
print(msg)

msg = '"Python" is a programing language.'
print(msg)

# 将每个单词的首字母大写
print(msg.title())

# 全部大写
print(msg.upper())

# 全部小写
print(msg.lower())

# 字符串通过 “+” 合并
print("Code" + " " + "Review")

msg = "   s t ron g "
print(msg)
# 剔除字符串两端空格
print(msg.strip())
# 剔除字符串左端空格
print(msg.lstrip())
# 剔除字符串右端空格
print(msg.rstrip())

# + - * / 加减乘除
## 乘方
print(3 ** 3)

# 转字符串
age = 23
print("Happy " + str(age) + "rd Birthday")

# Python 之禅
import this