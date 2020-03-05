import sys
sys.stdin = open('GNS_test_input.txt', 'r')
sys.stdout = open('GNS_test_output.txt', 'w', encoding='utf-8')
from pprint import pprint

map_t = [[0] * 100 for _ in range(100)]
map_t[ord('Z')][ord('R')] = 0
map_t[ord('O')][ord('N')] = 1
map_t[ord('T')][ord('W')] = 2
map_t[ord('T')][ord('H')] = 3
map_t[ord('F')][ord('O')] = 4
map_t[ord('F')][ord('I')] = 5
map_t[ord('S')][ord('I')] = 6
map_t[ord('S')][ord('V')] = 7
map_t[ord('E')][ord('G')] = 8
map_t[ord('N')][ord('I')] = 9

li = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for tc in range(1, T+1):
    t, N = input().split()
    N = int(N)
    nums = list(map(str,input().split()))
    counts = [0] * 10
    for num in nums:
        counts[map_t[ord(num[0])][ord(num[1])]] += 1
    s = ''
    for i in range(len(li)):
        s += (li[i] + ' ') * counts[i] 
    print('#{}\n {}'.format(tc, s))
  
#     # print(t, nums)
#     li = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
#     counts = [0] * 10
#     print('#{}'.format(tc))
#     for num in nums:
#         for i in range(len(li)):
#             if li[i] == num :
#                 counts[i] += 1
#     print('#{}'.format(tc))
        
#     for i in range(len(li)):
#         for j in range(counts[i]):
#             print(li[i], end=' ')

