# 1,2,3 일때 123 132 213 231 312 321순의 순열을 뽑는 알고리즘
# 단점 : 순차적으로 탐색하면서 백트랙킹을 하면서 가지치기가 필요한 경우,
#       재귀로 찾는 것이 좋다.

p = [1,2,2,3]
#1, 오름차순으로 정렬한다.
p.sort()
length = len(p)
stop = False
while True:
    # setp 1
    # 1. idx 찾기
    print(p)
    for i in range(length-1, -1, -1):
        # 2. 뒤에서부터 탐색하여 오름차순으로 정렬되어있을 때 왼쪽 인덱스를 저장
        if i == 0: # 3. 만약 내림차순으로 정렬이 되어있다면 더 이상 반복할 필요가 없으므로 종료
            stop = True
            break
        if p[i-1] < p[i]:
            idx = i-1 # 4. 교환 위치 인덱스 저장
            break
    if stop:
        break

    # step 2
    # 5. idx 자리에 있는 값보다 큰 p[k]를 찾아 p[idx], p[k] 스왑
    for k in range(length-1, -1, -1):
        if p[idx] < p[k]:
            p[idx], p[k] = p[k], p[idx]
            break

    # step 3
    # 6. idx+1 부터 끝까지의 배열을 오름차순으로 정렬
    # 7. 역순으로 정렬하는 것과 같은 말
    my_end_idx = length-1
    idx+=1
    while idx < my_end_idx:
        p[idx], p[my_end_idx] = p[my_end_idx], p[idx]
        idx += 1
        my_end_idx -= 1

