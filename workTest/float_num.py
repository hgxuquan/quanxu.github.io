while True:
    try:
        n = int(input())
        out_num = {}
        for i in range(n):
            index, value = map(int, input().split())
            if index in out_num:
                out_num[index] += value
            else:
                out_num[index] = value
        for k, v in out_num.items():
            print(k, v)
    except:
        break
