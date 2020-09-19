while True:
    try:
        src_list = []
        for c in input():
            if c.isalpha():
                src_list.append(c.lower())
            else:
                src_list.append(c)
        tar_char = input()
        if tar_char.isalpha():
            tar_char = tar_char.lower()
        print(src_list.count(tar_char))
    except:
        break
