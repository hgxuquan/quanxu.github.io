"""
[编程题] 扑克牌出牌
时间限制：10秒
空间限制：131072K
输入
第一行由13张组成，含3~A，2。3 4 5 6 7 8 9 10 J Q K A 2
第二行  用户的牌类型，可以为1/2/3/4/5/6张。分别为单个，对子，3个，4个，顺子（5张），连队（6张）

基本规则：
（1）第二行输入每手牌可能是个子，对子，三个，炸弹（四个）和顺子（连续5张），连对(6张)，不存在其他情况，
（2）除了炸弹可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较
（3）大小规则跟大家平时了解的常见规则相同，个子，对子，三个比较牌面大小；顺子比较最小牌大小；
炸弹大于前面所有的牌，炸弹之间比较牌面大小；

答案提示：
（1）除了炸弹之外，其他必须同类型比较。
（2）输入已经保证合法性，不用检查输入是否是合法的牌。


输入描述:
第一行由13张组成，含3~A，2。3 4 5 6 7 8 9 10 J Q K A 2
第二行  用户的牌类型，可以为1/2/3/4/5/6张。分别为单个，对子，3个，4个，顺子（5张），连队（6张）

输出描述:
扑克牌顺序不变，仍以空格隔开；如果不存在比较关系则输出ERROR。

输入例子1:
2 3 4 5 6 7 8 9 10 J Q K A
7 8 9 10 J

输出例子1:
8 9 10 11 12

输入例子1:
4 3 4 3 6 3 3 4 10 J 4 K A
8 8 8

输出例子1: 4 4 4 4
0 2 7 10
"""

map_dict = {
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
    '2': 15
}


def sorted_input(in_cards):
    in_list = list()
    # in_dict = dict()
    for i in range(len(in_cards)):
        card = in_cards[i]
        in_list.append((i, card, in_cards.count(card), map_dict[card]))
        # in_dict[card] = in_cards.count(card)
    return sorted(in_list, key=lambda x: (x[3], x[2]))


def find_max_4_card(sorted_list):
    pai = None
    for i in range(len(sorted_list) - 1, -1, -1):
        if 4 == sorted_list[i][2]:
            pai = in_ss[i][1]
            break
    s_index = list()
    for j in sorted_list:
        if pai == j[1]:
            s_index.append(j[0])
    return s_index


while True:
    try:
        in_card_list = input().split()
        other_pai = input().split()
        in_ss = sorted_input(in_card_list)
        print(in_ss)
        if len(other_pai) == 1:
            print(in_ss[-1][0])
        elif len(other_pai) in [2, 3, 4]:
            find_pai = None
            for i in range(len(in_ss) - 1, -1, -1):
                if len(other_pai) == in_ss[i][2]:
                    find_pai = in_ss[i][1]
                    break
            if find_pai is not None:
                card_index = list()
                for j in in_ss:
                    if find_pai == j[1]:
                        card_index.append(j[0])
                print(' '.join(list(map(str, card_index))))
            else:
                ll = find_max_4_card(in_ss)
                if len(ll) == 0:
                    print(-1)
                else:
                    print(' '.join(list(map(str, ll))))
        elif len(other_pai) == 5:
            pass
        elif len(other_pai) == 6:
            pass
    except:
        break
