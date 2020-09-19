# while True:
#     try:
#         count = int(input())
#         count_array = []
#         for aa in range(count):
#             count_array.append(int(input()))
#         count_list = list(set(count_array))
#         count_list.sort()
#         for bb in count_list:
#             print(bb)
#     except:
#         break

# while True:
#     try:
#         hex_str = input()
#         hex_number = int(hex_str, 16)
#         print(hex_number)
#     except:
#         break


while True:
    try:
        count = int(input())
        src_list = []
        for i in range(count):
            src_list.append(i)
        while len(src_list) != 1:
            cn = 0
            while cn != 2:
                src_list.append(src_list[0])
                src_list.pop(0)
                cn += 1
            src_list.pop(0)
        print(src_list[0])
    except:
        break
