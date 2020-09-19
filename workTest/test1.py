while True:
    try:
        m, n, r = map(int, input().split())
        m_list = list(map(int, input().split()))
        n_list = list(map(int, input().split()))
        result = []
        for a in m_list:
            n_index = 0
            for j in range(len(n_list)):
                if n_index >= j:
                    continue
                if a <= n_list[n_index] and n_list[n_index] - a <= r:
                    result.append([str(a), str(n_list[n_index])])
                    n_index = j
                    break
        for item in result:
            print(' '.join(item))
    except:
        break

# 2 3 4 5 6 7 8 9 10 J Q K A
# 7 8 9 10 J Q
# ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'J', 'K', 'Q']
# ['7', '8', '9', '10', 'J', 'Q']
