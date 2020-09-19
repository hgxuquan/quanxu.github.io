while True:
    try:
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        k = int(input())
        res = 0
        size1, arr1 = arr1[0], arr1[1:]
        size2, arr2 = arr2[0], arr2[1:]
        res_list = []
        for index1 in range(size1):
            for index2 in range(size2):
                res_list.append([index1, index2, arr1[index1] + arr2[index2]])
        res = sorted(res_list, key=lambda x: (x[2], x[0], x[1]))
        min_sum = 0
        for i in range(k):
            min_sum += res[i][2]
        print(min_sum)
    except:
        break
