phonenumber = '00-44   48 555 8361111'
def solution(S):
    S = S.strip().replace('-','').replace(' ','')
    ans = ''
    if len(S) % 3 == 0 or len(S) % 3 == 2:
        for j in range(len(S)):
            ans += S[j]
            if j % 3 == 2 and j < len(S)-1:
                ans += '-'
    else:
        for j in range(len(S)):
            ans += S[j]
            if j % 3 == 2 and j < len(S) - 2:
                ans += '-'
            if j == len(S) - 3:
                ans += '-'

    return ans
print(solution(phonenumber))
