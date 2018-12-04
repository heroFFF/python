import jieba
includes = {'宝钗','黛玉','凤姐','元春','探春','湘云','妙玉','迎春','惜春','巧姐','李纨','可卿'
            ,'香菱','宝琴','二姐','三姐','岫烟','李纹','李绮','宝珠','宝蟾','平儿','娇杏','瑞珠','袭人','紫鹃','晴雯'}
txt = open('红楼梦.txt','r', encoding='GB18030').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if word in includes:
        if word == '凤姐' or word == '熙凤':
            rword = '凤姐'
        elif word == '元春' or word == '贵妃':
            rword = '元春'
        elif word == '宝姑娘' or word == '宝钗':
            rword = '宝钗'
        elif word == '林姑娘' or word == '黛玉':
            rword = '黛玉'
        else:
            rword = word
        
        counts[rword] = counts.get(rword,0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse = True)
for i in range(20):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
