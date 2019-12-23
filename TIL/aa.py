value = 'abcdefghijklmnopqrstuvwxwz'
key = 0
for c in value:
    key ^= 1<<(ord(c)-ord('a'))
    print(key)