def solution(n, arr1, arr2):
    new_Arr = []
    for i in range(n):
        temp = str(bin(arr1[i] | arr2[i]))[2:]
    if len(temp) < n:
        temp = ' ' * (n-len(temp)) + temp
    temp = temp.replace('1','#')
    temp = temp.replace('0',' ')
    new_Arr.append(temp)
    return new_Arr