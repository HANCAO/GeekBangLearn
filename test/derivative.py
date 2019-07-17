# list_one = []
#
# for i in range(1, 11):
#     if i % 2 == 0:
#         list_one.append(i * i)
#
# print(list_one)
#
# list_two = [i*i for i in range(1, 11) if i % 2 == 0]
# print(list_two)
#
#
# # -------------------------------------------------------------------------------------
# zodiac_num = {}
#
# zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
#                u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'射手座')
#
# for i in zodiac_name:
#     zodiac_num[i] = 0
#
# zodiac_num = {i: 0 for i in zodiac_name}

# --------------------------------------------------------------------------------------

# 6-1  练习：字典的使用
# dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# pass  # 无用什么都不做
# dict_one['c'] = 'cake'
#
# print(dict_one)
#
# print(dict_one['d'])
#
# # 6-2 练习： 集合的使用
# dict_two = {i for i in 'hello'}
#
# dict_three = set('hello')
#
# print(dict_two)
# print(dict_three)  # {'h', 'l', 'e', 'o'} 集合中的元素不能重复

# ---------------------------------------------------------------------------------------
set_two = set('abcdefg')

set_three = {'a', 'f', 'z'}

print(set_two - set_three)
print(set_two | set_three)
print(set_two & set_three)
print(set_two ^ set_three)
