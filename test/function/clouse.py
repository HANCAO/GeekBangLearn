# def add():
# #     first = 1
# #     second = 2
# #     return first + second
# #
# #
# # print(add())  # 3
# # print(add)  # <function add at 0x0000023E2ABA3E18>
# #
# #
# # # 闭包 = 函数嵌套
# # def sum_num(first):
# #     def add_num(second):
# #         return first + second  # 内部函数引用外部变量
# #     return add_num  # 返回内部函数名称或引用
# #
# #
# # sum_num_second = sum_num(1)
# # print(type(sum_num_second))  # <class 'function'>
# # print(sum_num_second(2))  # 3


# def self_increase():
#     list_num = [0]  # 存储值且不可变
#
#     def add_one():
#         list_num[0] += 1
#         return list_num[0]
#     return add_one
#
#
# num = self_increase()
# print(num())  # 1
# print(num())  # 2
# print(num())  # 3
# print(num())  # 4
# print(num())  # 5

# def self_increase(first=0):  # 设定默认值为0
#     list_num = [first]  # 存储值且不可变
#
#     def add_one():
#         list_num[0] += 1
#         return list_num[0]
#     return add_one
#
#
# num = self_increase()  # 从0开始自增
# print(num())
#
# num5 = self_increase(5)  # 从5开始自增
# print(num5())  # 6
# print(num5())  # 7
#
# num10 = self_increase(10)  # 从10开始自增
# print(num10())  # 11
# print(num10())  # 12

# from dis import dis
# # dis模块可以反汇编python函数的字节码
#
#
# def counter2(first2=0):
#     cnt2 = first2
#
#     def add_one():
#         # nonlocal cnt2
#         cnt2 += 1
#         return cnt2
#     return add_one
#
#
# dis(counter2(3))

cnt2 = 1


# def counter():
#     def add_one():
#         a = cnt2 + 1
#         print(a)
#         return a
#
#     return add_one
#
#
# add_one = counter()
# add_one()   # output 2



