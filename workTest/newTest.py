def max_long_str(ss):
    if len(ss) < 2 or ss == ss[::-1]:
        return ss
    max_len = 1
    start = 0
    for i in range(1, len(ss)):
        # 偶数长度
        rr1 = ss[i - max_len:i + 1]
        # 奇数长度
        rr2 = ss[i - max_len - 1: i + 1]
        if i - max_len >= 0 and rr1 == rr1[::-1]:
            start = i - max_len
            max_len += 1
        if i - max_len - 1 >= 0 and rr2 == rr2[::-1]:
            start = i - max_len - 1
            max_len += 2
    print(max_len)
    return ss[start:start + max_len]


cn = 0


def process(arr, index, aim):
    global cn
    res = 0
    # if aim == 0:
    #     return 1
    if len(arr) == index:
        # print(cn)
        return 1 if aim == 0 else 0
    i = 0
    while arr[index] * i <= aim:
        temp = process(arr, index + 1, aim - arr[index] * i)
        # print(temp)
        # if temp == 0:
        #     global cn
        #     cn += 1
        # if cn == 1000:
        #     exit()
        if temp == 1:
            cn += 1
            print(cn)
        res = res + temp
        i = i + 1
    return res


if __name__ == '__main__':
    # in_ss = input()
    # in_ss = "abcdeedcd"
    # print(max_long_str(in_ss))

    arr1 = [5, 10, 25, 1]
    rr = process(arr1, 0, 1000)
    print(rr)
