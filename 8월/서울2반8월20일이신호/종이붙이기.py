# T = int(input())
#
# def paper(N):
#     if N == 20:
#         return 3
#     elif N == 10:
#         return 1
#     else:
#         return paper(N - 10) + 2 * paper(N - 20)
#
# for tc in range(1, T+1):
#     N = int(input())
#
#
#     print('#{} {}'.format(tc, paper(N)))

# 강사님 풀이
#
#
# def paper(w):
#
#     if w == n: # n은 목표너비///
#         return 1
#     if w > n:
#         return 0
#     return paper(w + 10) + 2 * paper(w + 20)
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     r = paper(0)
#     print(r)

#
def paper(w):
    if w == n: # n은 목표너비///
        memo[n] = 1
    if w > n:
    else:
        memo[w] = memo[w - 10] + 2 * memo[w - 20]

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    memo = [0] * (n + 1)
    paper(n)
    print(memo[n])
