# # 写入主角名字到文件中
# file1 = open('name.txt', 'w')  # 默认只读
# file1.write('诸葛亮')  # 写入文件(覆盖掉源文件)
# file1.close()  # 关闭文件
#
# file2 = open('name.txt')
# print(file2.read())
# file2.close()
#
# file3 = open('name.txt', 'a')  # 写入文件时在内容后追加而不是覆盖
# file3.write('刘备')
# file3.close()

# file4 = open('name.txt')
# print(file4.readline())  # 只查看文件单独一行
#
# file5 = open('name.txt')
# for line in file5.readlines():  # 读取多行
#     print(line)

# file6 = open('name.txt')
# print('当前文件指针位置为 %s' % file6.tell())
# print('当前读取了一个字符 %s' % file6.read(1))
# print('当前文件指针移动到 %s' % file6.tell())
#
# file6.seek(2, 0)
# print('运行seek操作后~')
# print('当前文件指针位置 %s' % file6.tell())
# print('当前读取了一个字符 %s' % file6.read(1))
# print('当前文件指针移动到 %s' % file6.tell())
# file6.close()

# from datetime import date
#
# current_date = date.today()
#
# file7 = open('current_date', 'w')
# file7.write(current_date.__str__())
# file7.close()
#
# file8 = open('current_date')
# print(file8.read(4))
# file8.close()

import datetime

now = datetime.datetime.now()
with open('current_time', 'w') as f:
    f.write(str(now))

with open('current_time', 'r') as f:
    text_4 = f.read(4)
    print(text_4)
