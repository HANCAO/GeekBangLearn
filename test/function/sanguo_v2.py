# 统计指定人物在小说中出现的次数
import re


def find_item(hero):
    with open('../text/sanguo.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        name_number = re.findall(hero, data)
        # print('人物 %s 在小说中出现了 %s 次' % (hero, len(name_number)))
    return len(name_number)


# 读取人物信息
name_dict = {}
with open('../text/name.txt', encoding='utf8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = name_num

# 利用字典统计小说中出现的次数 key为名字 value为出现次数
# print(name_dict)

# 排序输出
name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])
