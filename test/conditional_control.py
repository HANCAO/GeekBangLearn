# 条件语句的使用
# 5-1 判断字符串长度是否等于10 根据判断结果进行不同输出
# string = input('请输入字符')
# if len(string) == 10:
#     print('输入字符串长度等于10\n')
# elif len(string) > 10:
#     print('输入字符串长度大于10\n')
# else:
#     print('输入字符串长度小于10\n')

# 5-2 提示用户输入一个1-40之间的数字，
# 使用if语句根据输入数字的大小进行判断，
# 如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出

# number = int(input('请输入一个1~40之间的数字'))
# if (number >= 1) and (number <= 10):
#     print('输入数字在1-10范围内')
# elif (number >= 11) and (number <= 20):
#     print('输入数字在11-20范围内')
# elif (number >= 21) and (number <= 30):
#     print('输入数字在21-30范围内')
# elif (number >= 31) and (number <= 40):
#     print('输入数字在31-40范围内')

# if 1 <= number <= 10:
#     print('输入数字在1-10范围内')
# elif 11 <= number <= 20:
#     print('输入数字在11-20范围内')
# elif 21 <= number <= 30:
#     print('输入数字在21-30范围内')
# elif 31 <= number <= 40:
#     print('输入数字在31-40范围内')


# chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"  # 这里因为 猴年有2016 年，而2016可以被12整除，所以放到第一位
#
# year = int(input('请输入出生年份'))
#
# if chinese_zodiac[year % 12] == '虎':
#
#     print('哦~你属虎!')




