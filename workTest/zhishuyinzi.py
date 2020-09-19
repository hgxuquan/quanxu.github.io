while True:
    try:
        num = int(input())
        nn_list = []
        for i in range(2, num + 1):
            while num % i == 0 and num != 0:
                nn_list.append(str(i) + ' ')
                num = num // i
        print(''.join(nn_list))
    except:
        break
