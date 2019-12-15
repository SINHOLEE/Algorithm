# 1,2,3 일때 123 132 213 231 312 321순의 순열을 뽑는 알고리즘

p = [1,3,3,3,5,6,7,8,9,10]
#1, 오름차순으로 정렬한다.
p.sort()
length = len(p)
isEnd = True
cnt=1
while True:
    # 1. idx 찾기
    cnt +=1
    # print(p)
    for i in range(length-1, -1, -1):
        # 2. 뒤에서부터 탐색하여 오름차순으로 정렬되어있을 때 왼쪽 인덱스를 저장

        if i == 0: # 3. 만약 내림차순으로 정렬이 되어있다면 더 이상 반복할 필요가 없으므로 종료
            isEnd = False
            break
        if p[i-1] < p[i]:
            idx = i-1 # 4. 인덱스 저장
            break
    if isEnd == False:
        break
    # 5. idx자리에 있는 값보다 큰 p[k]를 찾아 p[idx], p[k] 스왑
    for k in range(length-1, -1,-1):
        if p[idx] < p[k]:
            p[idx], p[k] = p[k], p[idx]
            break
    # 6. idx+1 부터 끝까지의 배열을 오름차순으로 정렬
    # 7. 역순으로 정렬하는 것과 같은 말
    my_end_idx = length-1
    idx+=1
    while idx < my_end_idx:
        p[idx], p[my_end_idx] = p[my_end_idx], p[idx]
        idx += 1
        my_end_idx -= 1
print(cnt)

print(7*6*5*4*3*2*1*3*2*1)