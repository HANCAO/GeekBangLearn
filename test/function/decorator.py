# import time  # 引入 time库

# print(time.time())  # 1563364425.8325663  输出从1970年到此刻的秒数
#
#
# def i_can_sleep():
#     time.sleep(5)  # 使得程序暂停执行5秒
#
#
# i_can_sleep()
# import time
#
#
# def i_can_sleep():
#     time.sleep(1)
#
#
# start_time = time.time()
# i_can_sleep()
# end_time = time.time()
#
# print('程序运行了 %s 秒' % (end_time - start_time))  # 程序运行了 1.0007772445678710938 秒


import time


def timer(func):  # 闭包传递的是函数 func
    def wrapper():
        start_time = time.time()
        func()  # 内部函数使用的也是函数 func()
        end_time = time.time()
        print('该程序运行了 %s 秒' % (end_time - start_time))
    return wrapper  # 使用闭包


@timer  # 语法糖调用装饰器
def i_can_sleep():
    time.sleep(1)


# 可以直接使用
i_can_sleep()  # 该程序运行了 1.0001416206359863 秒
