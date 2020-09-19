while True:
    try:
        src_list = input().split(';')
        point = [0, 0]
        for ss in src_list:
            if len(ss) in [2, 3] and ss[0] in ['A', 'S', 'W', 'D'] and ss[1].isdigit():
                if len(ss) == 3 and ss[2].isdigit():
                    if ss[0] == 'A':
                        point[0] -= int(ss[1:])
                    elif ss[0] == 'S':
                        point[1] -= int(ss[1:])
                    elif ss[0] == 'W':
                        point[1] += int(ss[1:])
                    elif ss[0] == 'D':
                        point[0] += int(ss[1:])
                if len(ss) == 2:
                    if ss[0] == 'A':
                        point[0] -= int(ss[1])
                    elif ss[0] == 'S':
                        point[1] -= int(ss[1])
                    elif ss[0] == 'W':
                        point[1] += int(ss[1])
                    elif ss[0] == 'D':
                        point[0] += int(ss[1])
        print(','.join(map(str, point)))
    except:
        break
