import sys
#sys.stdin = open("input.txt", "r")
L, C = map(int, sys.stdin.readline().split())
chars = list(sys.stdin.readline().split())
chars.sort()
aaaa = 0
def crypto(chars, curr,curr_index):
    # print(curr)
    global aaaa
    aaaa+=1
    if len(curr) == L:
        if 'a' in curr or 'e' in curr or 'o' in curr or 'i' in curr or 'u' in curr:
            if len(curr.replace('a','').replace('e','').replace('o','').replace('i','').replace('u',''))>=2:
                print(curr)
                return
    if curr_index == C:
        return
    crypto(chars, curr + chars[curr_index], curr_index + 1)
    crypto(chars, curr, curr_index + 1)

crypto(chars, '',0)
print(aaaa)