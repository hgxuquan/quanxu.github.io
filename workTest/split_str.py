while True:
    try:
        in_str = input()
        cn = 8 - len(in_str) % 8
        if cn < 8:
            for i in range(cn):
                in_str += '0'
        for i in range(0, len(in_str), 8):
            print(in_str[i:i + 8])
    except:
        break
