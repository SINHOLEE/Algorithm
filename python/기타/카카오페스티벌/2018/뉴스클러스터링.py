
str1 = 'FRANCE'
str2 = 'french'

def solution(str1, str2):
    num = 65536

    zip1 = {}
    zip2 = {}
    for i in range(len(str1)-1):
        temp = ''
        for j in str1[i:i+2]:
            if ord(j) >= 65 and ord(j) <= 90:
                temp += j
            elif ord(j) >= 97 and ord(j) <= 122:
                temp += chr(ord(j) - 32)
            else:
                break
        if len(temp) == 2:
            if temp not in zip1:
                zip1[temp] = 1
            else:
                zip1[temp] += 1
    for i in range(len(str2) - 1):
        temp = ''
        for j in str2[i:i + 2]:
            if ord(j) >= 65 and ord(j) <= 90:
                temp += j
            elif ord(j) >= 97 and ord(j) <= 122:
                temp += chr(ord(j) - 32)
            else:
                break
        if len(temp) == 2:
            if temp not in zip2:
                zip2[temp] = 1
            else:
                zip2[temp] += 1
    nd = 0
    for k, v in zip1.items():
        if zip2.get(k) != None:
            nd += min(zip1[k], zip2[k])
    dummy1 = set(zip1)
    dummy2 = set(zip2)
    dummy1.update(dummy2)
    xor = 0
    for i in dummy1:
        if zip2.get(i) == None:
            b = 0
        else:
            b = zip2.get(i)
        if zip1.get(i) == None:
            a = 0
        else:
            a = zip1.get(i)
        xor += max(a, b)
    if xor == 0:
        answer = 1
    else:
        answer = int((nd / xor) * num)
    return answer
print(solution(str1, str2))
