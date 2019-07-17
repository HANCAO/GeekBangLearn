file_name = open('../text/name.txt', encoding='utf8')
try:
    for line in file_name:
        print(line)
finally:
    file_name.close()
# try finally 不优雅

with open('../text/name.txt', encoding='utf8') as file_name:
    for line in file_name:
        print(line)
# 出现异常会自动关闭文件

# 諸葛亮|關羽|劉備|曹操|孫權|關羽|張飛|呂布|周瑜|趙雲|龐統|司馬懿|黃忠|馬超
# 諸葛亮|關羽|劉備|曹操|孫權|關羽|張飛|呂布|周瑜|趙雲|龐統|司馬懿|黃忠|馬超
