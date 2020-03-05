# class Solution:
#     def reverse(self, x):
#         x = list(str(x))
#         res = ""
#         while x:
#             a = x.pop()
#             if a == '-':
#                 res = a + res
#             else:
#                 res += a
#         res = int(res)
#         if -1 * 2 **(31) <= res <= 2 ** 31:
#             return res
#         else:
#             return 0

class Solution:
    def reverse(self, x):
        temp = 1
        if x < 0:
            temp = -1
        x *= temp
        res = 0
        while x != 0:
            moc = x % 10
            x = x // 10
            res = res * 10 + moc
        if-1 * 2 **(31) <= res * temp <= 2 ** 31:
            return temp * res
        else:
            return 0


