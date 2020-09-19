while True:
    try:
        ss = bin(int(input()))
        cn = 0
        for i in ss:
            if i == '1':
                cn += 1
        print(cn)
    except:
        break
