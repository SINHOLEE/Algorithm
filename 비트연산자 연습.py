def get_nth_bit(n, nth):
    return n & (1 << nth)


print('10진수 100을 2진수로 변환한 값:', bin(100))
print(get_nth_bit(100, 2))

print(get_nth_bit(100, 7))