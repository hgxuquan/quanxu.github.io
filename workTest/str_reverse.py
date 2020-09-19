while True:
    try:
        src_list = input().split()
        src_list.reverse()
        print(' '.join(src_list))
    except:
        break
