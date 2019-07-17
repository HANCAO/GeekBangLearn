def func(a, b, c):
    print('a = %s' % a)
    print('b = %s' % b)
    print('c = %s' % c)


func(1, 2, 3)
# a = 1
# b = 2
# c = 3

func(1, c=3, b=2)  # 指定参数后，可以更换参数类型
# a = 1
# b = 2
# c = 3


def howlong(first, *other):  # 可变长参数 在参数前加上 * 表示调用函数时可以使用一个或多个参数
    print((len(first) + len(other)))


howlong('abc', 2, 3, 4, 5)  # 7
