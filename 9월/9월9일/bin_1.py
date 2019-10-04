def htod(a):
    A = ord('A')
    zero = ord('0')

    if ord(a) >= A:
        result = ord(a) - A + 10

    else:
        result = ord(a) - zero

    return result

def dtob_4(res):
    string = ['', '', '', '']

    for i in range(3, -1, -1):
        if res & 1:
            string[i] = str(1)
        else:
            string[i] = str(0)
        res >>= 1
    return ''.join(map(str, string))



T = int(input())

for tc in range(1, T+1):
    N, hex_num = map(str, input().split())
    N = int(N)
    s = ''
    for n in range(N):
        s += dtob_4(htod(hex_num[n]))
    print('#%s %s' % (tc, s))