# 函数练习1
# 创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和


def sum(num, * other):
    sum = num
    for i in range(1 + len(other)):
        if i < len(other):
            sum += other[i]
        i += 1
    return sum


print('输入数之和为：%s' % sum(1, 2, 3))


# 创建一个函数，传入n个整数，返回其中最大的数和最小的数
def max_and_min(num, * other):
    max_value = num
    min_value = num
    for i in range(1 + len(other)):
        if i < len(other):
            if other[i] >= max_value:
                max_value = other[i]
            elif other[i] <= min_value:
                min_value = other[i]
        i += 1
    return '输入的数中最大值为 : %s ;最小的值为 : %s' % (max_value, min_value)


print(max_and_min(1, 2, 3, 100))


# 创建一个函数，传入一个参数n，返回n的阶乘
def factorial(n):
    factorial_value = 1
    for num in range(1, n+1):
        if num <= n:
            factorial_value *= num
        num += 1
    return factorial_value


n = int(input('请输入n值:'))
print('%s 的阶乘为：%s' % (n, factorial(n)))
