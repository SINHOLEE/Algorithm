T = int(input())

for tc in range(1, T+1):
    N = float(input())
    string = ''
    for e in range(1, 13):
        minus_e = -1 * e
        target = 2 ** minus_e
        if N >= target and N != 0:
            N -= target
            string += '1'
        elif N < target and N != 0:
            string += '0'

    if N == 0:
        print('#%s %s' % (tc, string))
    else:
        print('#%s overflow' % tc)