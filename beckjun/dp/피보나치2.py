zero = [1, 0] + [0] * 39
one = [0, 1] + [0] * 39

for i in range(2, 41):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]
print(zero)
print(one)
T = int(input())

for tc in range(T):
    n = int(input())
    print(zero[n], one[n])