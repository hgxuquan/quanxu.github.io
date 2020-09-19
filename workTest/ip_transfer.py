# 用lambda的方式，IP地址转换到整数
# ip_to_int = lambda x: sum([256 ** j * int(i) for j, i in enumerate(x.split('.')[::-1])])
# print(ip_to_int('10.0.3.19'))


def ip2int(x):
    return sum([256 ** j * int(i) for j, i in enumerate(x.split('.')[::-1])])


# 用lambda的方式，整数toIP 地址 一行代码搞定
# int_to_ip = lambda x: '.'.join([str(x // (256 ** i) % 256) for i in range(3, -1, -1)])
# print(int_to_ip(167969729))

def int2ip(x):
    return '.'.join([str(x // (256 ** i) % 256) for i in range(3, -1, -1)])


while True:
    try:
        ip_data = input()
        int_data = input()
        # print(ip_data)
        # print(int_data)
        print(ip2int(ip_data))
        print(int2ip(int(int_data)))
    except:
        break
