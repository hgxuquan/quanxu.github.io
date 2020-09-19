"""
test1:
4 5 5
1 5 5 10
1 3 8 8 20

1 1
5 8
5 8

test2:
4 5 5
21 25 25 30
1 3 8 8 20

"""

while True:
    try:
        m, n, r = map(int, input().split())
        m_list = list(map(int, input().split()))
        n_list = list(map(int, input().split()))
        result = []
        flag = False
        for a in m_list:
            if flag:
                break
            count = 0
            for b in n_list:
                count += 1
                if a <= b and b - a <= r:
                    result.append([str(a), str(b)])
                    break
            if count == len(n_list):
                flag = True
        for item in result:
            print(' '.join(item))
    except:
        break
