# while True:
#     try:
#         st = input()
#         letter_list = list(st)
#         letter_dict = {}
#         for i in letter_list:
#             if i not in letter_dict.keys():
#                 letter_dict[i] = 1
#             else:
#                 letter_dict[i] += 1
#         n = min(letter_dict.values())  # 求字典的value下的最小值，返回的是value值，
#         for i in st:
#             if n == letter_dict[i]:
#                 letter_list.remove(i)
#         print(''.join(letter_list))
#     except:
#         pass


while True:
    try:
        in_str = input()
        in_set = set(in_str)
        cn_dict = {}
        for c in in_set:
            cn_dict[c] = in_str.count(c)
        cn_min = min(cn_dict.values())
        for k, v in cn_dict.items():
            if v == cn_min:
                in_str = in_str.replace(k, '')
        print(in_str)
    except:
        break
