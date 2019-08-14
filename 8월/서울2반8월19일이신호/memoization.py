# # memoization

#
# def fibo(n):
#     global memo
#     if len(memo) <= n and n >= 2:
#         memo += [fibo(n-1) + fibo(n-2)]
#
#     return memo[n]
#
# memo = [0, 1]
#
# ans = fibo(10)
#
# print(ans, memo)
# #
# 재귀함수
# def fibo1(n):
#     if n < 2 and 0 <= n:
#         return n
#     elif n >= 2:
#         return fibo1(n-1) + fibo1(n-2)
#     else:
#         return '음수입니다.'
# ans = fibo1(35)
# print(ans)

#  동적계획법



def fibo2(n):
    memo = [0, 1]

    if n >= 2:
        for i in range(2, n+1):
            memo += [memo[i-1] + memo[i-2]]
        return memo[n]
    else:
        return memo[n]

print(fibo2(6))