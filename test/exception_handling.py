# try:
#     year = int(input('input year:'))
# except (ValueError, AttributeError, KeyError):
#     print('请输入数字')
#
# try:
#     print(1/0)
# except Exception as e:
#     print(e)
#
# print(1/0)

# try:
#     raise NameError('helloError')
# except NameError as e:
#     print(e)

# try:
#     try:
#         file_new = open('name1.txt')
#     except Exception as e:
#         print(e)  # [Errno 2] No such file or directory: 'name1.txt'
#     finally:
#         file_new.close()  # NameError: name 'file_new' is not defined
# except Exception as e:
#     print(e)
# finally:
#     pass

# 练习
# 8-1 在Python程序中，分别使用未定义变量、访问列表不存在的索引、访问字典不存在的关键字观察系统提示的错误信息
try:
    # i = j  # name 'j' is not defined
    list_people = ['hschen', 'hansichen']
    # print(list_people[2])  # list index out of range

    dict_place = {'zj': 'lh', 'sx': 'lv'}
    print(dict_place['fj'])  # 'fj'
except Exception as e:
    print(e)

# 8-2 通过Python程序产生IndexError，并用try捕获异常处理
try:
    list_normal = ['hschen.top', 'kuying.club']
    print(list_normal[2])
except IndexError as e:
    print('超出了列表索引 %s' % e)
