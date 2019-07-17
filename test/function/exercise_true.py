# 1. 创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和
def func1():
    two_num = input('请输入两个数字，用空格做分隔：')
    # 检查用户输入是否合法
    func2(two_num)
    num1, *_, num2 = list(two_num)  # list(string) 函数可以把string类型的变量按一个字节一个字节的分隔成单个单个的字符
    print(int(num1) + int(num2))


def func2(check_number):
    pass

func1()


# 2. 创建一个函数，传入n个整数，返回其中最大的数和最小的数


def func3(*nums):
    print('最大数为 ：%s' % (max(list(nums))))
    print('最小数为 ：%s' % (min(list(nums))))


func3(1, 2, 3, 4, 250)


# 3. 创建一个函数，传入一个参数n，返回n的阶乘
# 使用递归

def fact(num3):
    if num3 == 0 or num3 == 1:
        return 1
    else:
        return num3 * fact(num3 -1)


print(fact(10))


# 使用高阶函数
from functools import reduce
num4 = 10
print(reduce(lambda x, y: x * y, range(1, num4 + 1)))
