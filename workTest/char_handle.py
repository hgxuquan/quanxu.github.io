# 题目描述
# 编写一个程序，将输入字符串中的字符按如下规则排序。
#
# 规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
# 如，输入： Type 输出： epTy
#
# 规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
# 如，输入： BabA 输出： aABb
#
# 规则 3 ：非英文字母的其它字符保持原来的位置。
# 如，输入： By?e 输出： Be?y
#
# 注意有多组测试数据，即输入有多行，每一行单独处理（换行符隔开的表示不同行）
# 示例1
# 输入
# A Famous Saying: Much Ado About Nothing (2012/8).
# 输出
# A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).


def handle_str(s):
    a, L = [], len(s)
    for i in range(L):
        if s[i].isalpha():  # 判断是否为字母
            a.append((s[i], s[i].lower(), i))  # 在列表中添加小列表（这个元素，以及小写，和位置）
    # lambda是匿名函数，x是参数，冒号后边是表达式,#这个的意思是以key函数的顺序排序,也就是先紧着第二个的顺序排序，
    # 然后是第三个，第一个重要性最低。注意的是，原列表中的元素顺序不变
    b = sorted(a, key=lambda x: (x[1], x[2], x[0]))
    result = ''
    for i in range(L):
        if s[i].isalpha():
            result += b[0][0]
            del b[0]  # 删除这个元素，后边的元素依次往前进1
        else:
            result += s[i]
    return result


try:
    while True:
        print(handle_str(input()))
except:
    pass
