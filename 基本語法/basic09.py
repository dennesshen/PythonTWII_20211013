# Python 基本資料結構
# list   列表[]    (元素內容可以重複, 元素內容可以修改)
# tuple  列表()    (唯讀, Fast)
# set    列表{}    (元素內容不可重複, 元素內容可以修改)
# dict   字典列表{} (元素內容可以重複, 元素內容可以修改)

#  1. list 列表
import re

scores1 = [100, 90]
scores2 = [80, 70]
scores1[1] = 95
print(scores1)
scores1.append(70)
scores1.append("23adf")
print(scores1)
scores3 = scores2 + scores1
print(scores3)

# tuple 列表 -> 不可增加修改
score = (100, 90)
print(type(score))

# list 與 tuple 互轉
scores = (100, 90)
scores = list(scores)
print(type(scores), scores)
scores = tuple(scores)
print(type(scores), scores)

# set 列表 -> 不重複並且按升冪排序
empIds = [1, 3, 5, 2, 3, 1]
empIds = set(empIds)
print(type(empIds), empIds)
print(len(empIds))

# dict 字典列表(Key:value)
a = {"symbol" : "2330.TW", "price": 599 }
b = {"symbol" : "2317.TW", "price": 108 }
c = {"symbol" : "3008.TW", "price": 2080 }
prices = [a, b, c]
print(type(prices), prices)
for p in prices:
    print(p, p.get("symbol"), p.get("price"))

# 切割字串
# 股名、價格、殖利率、本益比、股價淨值比
s = "2330.TW,599,1.67,28.03,7.8"
print(type(s))
s = s.split(",")
print(type(s), s, "本益比", s[3])

# 多符號切割(需要import re)
s = "2330.TW,599!1.67#28.03%7.8"
s = re.split('[,!#%]', s)
print(type(s), s, "本益比", s[3])

#split 轉 dict
s = "股名=2330.TW,價格=599,殖利率=1.67,本益比=28.03,股價淨值比=7.8"
s = dict( ex.split("=") for ex in s.split(",") )
print(type(s), s, s.get("本益比"))

