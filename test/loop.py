# for循环
# chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
#
# for cz in chinese_zodiac:  # 遍历生肖
#     print(cz)
#
# for i in range(1, 13):  # 遍历1~12
#     print(i)
#
# for year in range(1998, 2020):
#     print('%s 年的生肖为 %s' % (year, chinese_zodiac[year % 12]))

# while循环
# import time
#
# num = 5
# while True:
#     # print('a')
#     #
#     # num = num + 1
#     #
#     # if num > 10:
#     #     break  # 结束当前运行程序
#
#     num = num + 1
#
#     if num == 10:
#         continue  # 结束当前循环，继续执行接下来符合条件的循环语句
#
#     print(num)
#     time.sleep(1)

# for循环和if的嵌套
# zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
#                u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'射手座')
#
# zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
#                (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# while True:
#     int_month = int(input('请输入月份'))
#     int_day = int(input('请输入日期'))
#
#     for zd_num in range(len(zodiac_days)):
#         if zodiac_days[zd_num] >= (int_month, int_day):
#             print(zodiac_name[zd_num])
#             break
#         elif int_month == 12 and int_day > 23:
#             print(zodiac_name[0])
#             break


# while循环和if的嵌套
# n = 0
# int_month = int(input('请输入月份'))
# int_day = int(input('请输入日期'))
# while zodiac_days[n] < (int_month, int_day):
#     if int_month == 12 and int_day > 23:
#         break
#     n += 1
#
# print(zodiac_name[n])


# 练习
# 5-3 使用for语句输出1-100之间的所有偶数
for i in range(1,101):
    if i % 2 == 0:
        print(i)
    else:
        continue

# 5-4 使用while语句输出1-100之间能够被3整除的数字
j = 0
while j <= 100:
    j += 1
    if j % 3 == 0:
        print(j)
    else:
        continue
