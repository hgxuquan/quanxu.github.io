import sys

last_code = ['254', '252', '248', '240', '224', '192', '128', '0']

# 分别对应A、B、C、D、E、错误IP地址或错误掩码、私有IP
address = [0, 0, 0, 0, 0, 0, 0]


def check_ip(ip):
    if len(ip) != 4 or '' in ip:
        return False
    else:
        for i in range(4):
            if int(ip[i]) < 0 or int(ip[i]) > 255:
                return False
            else:
                return True


def check_mask(mask):
    if len(mask) != 4:
        return False
    else:
        if mask[0] == '255':
            if mask[1] == '255':
                if mask[2] == '255':
                    if mask[3] in last_code:
                        return True
                    else:
                        return False
                elif mask[2] in last_code and mask[3] == '0':
                    return True
                else:
                    return False
            elif mask[1] in last_code and mask[2] == mask[3] == '0':
                return True
            else:
                return False
        elif mask[0] in last_code and mask[1] == mask[2] == mask[3] == '0':
            return True
        else:
            return False


while True:
    Input = sys.stdin.readline().strip()
    if Input == '':
        break
    ipList = Input.split('~')[0]
    maskList = Input.split('~')[1]
    ip = ipList.split('.')
    mask = maskList.split('.')
    if check_ip(ip) and check_mask(mask):
        if 1 <= int(ip[0]) <= 126:
            address[0] += 1
        if 128 <= int(ip[0]) <= 191:
            address[1] += 1
        if 192 <= int(ip[0]) <= 223:
            address[2] += 1
        if 224 <= int(ip[0]) <= 239:
            address[3] += 1
        if 240 <= int(ip[0]) <= 255:
            address[4] += 1
        if int(ip[0]) == 10 or (int(ip[0]) == 172 and 16 <= int(ip[1]) <= 31) or (
                int(ip[0]) == 192 and int(ip[1]) == 168):
            address[6] += 1
    else:
        address[5] += 1
    # print(Input)
print(' '.join(map(str, address)))
