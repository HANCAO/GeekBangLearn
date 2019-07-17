# # 不带参数装饰器函数写作模版
# def out(func):
#     def inner():
#         print('start')
#         func()
#         print('stop')
#     return inner
#
#
# # 带参数装饰器函数使用
# def new_tips(argv):
#     def tips(func):
#         def change(a, b):  # 注意这里要带入被装饰函数里的参数
#             print('start %s ' % (argv))
#             func(a, b)  # 这里也要
#             print('stop')
#         return change
#     return tips
#
#
# @new_tips('add')
# def add(a, b):
#     print((a + b))
#
#
# @new_tips('sub')
# def sub(a, b):
#     print(a - b)
#
#
# print(add(1, 2))
# # start add
# # 3
# # stop
# # None
# print(sub(1, 2))
# # start sub
# # -1
# # stop
# # None


# def func():
#     return 1 + 2
#
#
# print(func.__name__)  # 获取指定函数的函数名
