dict1 = {}

print(type(dict1))  # <class 'dict'>

dict2 = {'length': 80, 'width': 80}

print(dict2)  # {'length': 80, 'width': 80}

dict2['height'] = 80  # 增加值

print(dict2)

# ------------------------------------------------------------------------------------------
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

# 记录星座出现的次数 并初试化次数为0
zodiac_num = {}

# 不够优雅 使用字典推导式
# for i in zodiac_name:
#     zodiac_num[i] = 0
zodiac_num = {i: 0 for i in zodiac_name}

# print(zodiac_num)

# 记录生肖出现的次数 并初始化次数为0
chinese_zodiac_num = {}

# for j in chinese_zodiac:
#     chinese_zodiac_num[j] = 0
chinese_zodiac_num = {j: 0 for j in chinese_zodiac}

# print(chinese_zodiac_num)


while True:

    # 获取用户输入的出生日期
    year = int(input('请输入出生年份'))
    month = int(input('请输入出生月份'))
    day = int(input('请输入出生日期'))

    n = 0
    while zodiac_days[n] < (month, day):
        if month == 12 and day > 23:
            break
        n += 1
    print('%s 月 %s 日星座为 %s' % (month, day, zodiac_name[n]))  # 输出用户星座

    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))  # 输出用户生肖

    # 记录星座数目 增一
    zodiac_num[zodiac_name[n]] += 1
    # 记录生肖数目 增一
    chinese_zodiac_num[chinese_zodiac[year % 12]] += 1

    # 遍历星座统计次数 keys()方法表示字典中的全部key dict[key]=value
    for each_key in zodiac_num.keys():
        print('星座 %s 有 %d 个' % (each_key, zodiac_num[each_key]))

    for each_key in chinese_zodiac_num.keys():
        print('生肖 %s 有 %d 个' % (each_key, chinese_zodiac_num[each_key]))
