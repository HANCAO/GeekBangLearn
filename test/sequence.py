# # 字符串常用操作
# chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"  # 这里因为 猴年有2016 年，而2016可以被12整除，所以放到第一位
#
# year = 1998
#
# print(chinese_zodiac[year % 12])
#
# # 元组
# zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
#                u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'射手座')
#
# zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
#                (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
#
# birth_day = (7, 24)
#
# zodiac_day = filter(lambda x: x <= birth_day, zodiac_days)
# # print(zodiac_day) <过滤器对象位于0x0000023382C3B3C8>
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])

# 练习 元组的基本操作
# tuple1 = ("ab", 'cd')
# print(tuple1[-2])
# tuple2 = ("ef", "ij")
# tuple3 = tuple1 + tuple2
# print(len(tuple3))

# 列表(可以修改添加删除，元组不可)
list1 = ["abc", "xyz"]
list1.append('X')
print(list1)
list1.remove("xyz")
print(list1)

# 练习 列表基本操作
# list1 = [1, 2, 3, 4, 5]
# list1.append(100)  # 增加列表中的数
# print(list1)
# list1.remove(100)  # 删除列表指定数
# print(list1)
# print(list1[:3])  # 列表前三个数
# print(list1[-1])  # 列表最后一个数
