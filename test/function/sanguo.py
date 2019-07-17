# 读取三国文本
file_sanguo = open('../text/sanguo.txt', encoding='GB18030')  # 编码以适应繁体中文
print(file_sanguo.read().replace('\n', ''))  # 读取文本并将文本中的换行替换为空
file_sanguo.close()

# 读取人物名字
file_name = open('../text/name.txt', encoding='utf8')
print(file_name.read().split('|'))  # 去掉文本中的 | ,并将数据存储到列表中 ['諸葛亮', '關羽', ...]
file_name.close()

# 读取兵器库
file_weapon = open('../text/weapon.txt', encoding='utf8')
data_weapon = file_weapon.readlines()
i = 1
for line in data_weapon:
    if i % 2 == 1:  # 只输出奇数行
        print(line.strip('\n'))  # 去掉文本中的 换行符
    i += 1


def func(filename):
    print(open('../text/'+filename, encoding='utf8').read())


func('name.txt')
func('weapon.txt')
