while True:
    try:
        ss = input()
        new_set = set()
        out_list = []
        for c in range(len(ss) - 1, -1, -1):
            if ss[c] in new_set:
                continue
            else:
                out_list.append(ss[c])
                new_set.add(ss[c])
        print(''.join(out_list))
    except:
        break
