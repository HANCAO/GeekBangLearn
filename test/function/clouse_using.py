def line(a, b):  # 固定直线方程的常数项
    # def constant(x):  # 传入直线上x的值
    #     return a + b * x
    return lambda x: a + b * x  # 使用Lambda表达式使得代码更优雅
    # return constant


# 定义一条直线 a = 1 b = 2
# 当 x = 3 时
line_one = line(1, 2)
print(line_one(3))  # 7　(1 + 2 * 3)
# 当 x = 4
print(line_one(4))  # 9

# 定义另一条直线 a = 2 b = 3
# 当 x = 5
line_two = line(2, 3)
print(line_two(5))  # 17 (2 + 3 * 5)
