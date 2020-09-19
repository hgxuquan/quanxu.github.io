# while True:
#     try:
#         N = int(input())
#         tmp_begin = 1  # 第一行的数
#         for i in range(1, N + 1):
#             begin = tmp_begin  # 每行的开头
#             if i == N:
#                 print(begin)
#             else:
#                 print(begin, end=" ")
#             for j in range(i + 1, N + 1):
#                 begin += j
#                 if j == N:
#                     print(begin)
#                 else:
#                     print(begin, end=" ")
#             tmp_begin += i
#     except:
#         break

while True:
    try:
        N = int(input().strip())
        tmp_begin = 1
        for i in range(1, N + 1):
            begin = tmp_begin
            if i == N:
                print(begin)
            else:
                print(begin, end=" ")
            for j in range(i + 1, N + 1):
                begin += j
                if j == N:
                    print(begin)
                else:
                    print(begin, end=" ")
            tmp_begin += i
    except:
        break
