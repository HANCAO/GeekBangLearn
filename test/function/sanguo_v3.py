# import re
#
#
# # 统计指定兵器在小说中出现的次数
# def find_weapon_item(weapon):
#     with open('../text/sanguo.txt', encoding='GB18030') as f:
#         data = f.read().replace('\n', '')
#         weapon_number = re.findall(weapon, data)
#     return len(weapon_number)
#
#
# # 读取兵器库信息
# weapon_dict = {}
# with open('../text/weapon.txt', encoding='utf8') as f:
#     i = 1
#     for line in f:
#         if i % 2 == 1:
#             # print(line.strip())
#             weapon_num = find_weapon_item(line.strip())
#             weapon_dict[line.strip()] = weapon_num
#         i += 1
#
# weapon_sorted = sorted(weapon_dict.items(), key=lambda item: item[1], reverse=True)
# print(weapon_sorted[0:10])

import re


def find_main_charecters(charecter_name):
    with open('../text/sanguo.txt', encoding='gb18030') as f:
        data = f.read().replace("\n", "")
        name_num = re.findall(charecter_name, data)
        # print('主角 %s 出现了%s 次'%(charecter_name,len(name_num)))
    return charecter_name, len(name_num)


name_dict = {}
with open('../text/name.txt', encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            char_name, char_number = find_main_charecters(n)
            name_dict[char_name] = char_number

weapon_dict = {}
with open('../text/weapon.txt', encoding='utf-8') as f:
        i = 1
        for line in f:
             if i%2 == 1:
                weapon_name, weapon_number = find_main_charecters(line.strip())
                weapon_dict[weapon_name] = weapon_number
             i = i+1


name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])

weapon_sorted = sorted(weapon_dict.items(), key=lambda item: item[1], reverse=True)
print(weapon_sorted[0:10])
