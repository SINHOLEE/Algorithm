import sys
sys.stdin = open('GNS_test_input.txt', 'r')
sys.stdout = open('GNS_test_output.txt', 'w', encoding='utf-8')

T = int(input())
for tc in range(1, T+1):
    t, N = input().split()
    N = int(N)
    nums = list(map(str,input().split()))
    # print(t, nums)
    li = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    dic = {'ZRO' : 0, 'ONE' : 0, 'TWO' : 0, 'THR' : 0, 'FOR' : 0, 'FIV' : 0, 'SIX' : 0, 'SVN' : 0, 'EGT' : 0, 'NIN' : 0}
    for num in nums:
        dic[num] += 1
    temp = []
    for l in li:
        temp += [l] * dic[l]
    print(t)
    print(' '.join(map(str,temp)))