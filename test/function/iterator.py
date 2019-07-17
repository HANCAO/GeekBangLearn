# for i in range(10, 20, 2):
#     print(i)
#
# list1 = [1, 2, 3]
# for i in list1:
#     print(i)

# list2 = [1, 2, 3]  # 定义列表
# it = iter(list2)   # 使用迭代器赋值
# print(next(it))  # 迭代迭代器
# print(next(it))  # 每调用一次，指向下一个值
# print(next(it))
# print(next(it))  # 超出列表长度报错  StopIteration


def float_range(start, end, step):
    temp = start  # 定义临时变量存储 start的值
    while temp < end:
        yield temp  # 区别与直接全部输出所有的值，使用yield 可以每调用一次next输出一个值
        temp += step  # 增加步长


for i in float_range(10, 20, 0.5):
    print(i)
