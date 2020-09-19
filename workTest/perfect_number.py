def count(x):
    if x <= 0 or x > 500000:
        return -1
    cn = 0
    for i in range(1, x):
        num = 0
        for k in range(1, i):
            if i % k == 0:
                num += k
        if i == num:
            cn += 1
    return cn


# in_data = input()
# print(count(int(in_data)))

# while True:
#     try:
#         print(int(input()) + int(input()))
#     except:
#         break

while True:
    try:
        x = int(input())
        cn = 0
        for n in range(2, x + 1):
            factors = [i for i in range(2, n // 2 + 1) if n % i == 0]
            if (sum(factors) + 1) == n:
                cn += 1
        print(cn)
    except:
        break
