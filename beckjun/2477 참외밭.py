K = int(input())

arr = [0] * 8
for i in range(1, 7):
    temp = list(map(int, input().split()))
    arr[i] = temp[1]

arr[0] = arr[6]
arr[7] = arr[1]

odd_max = 0
even_max = 0

for j in range(1, 7):
    if j % 2:  # 홀수번 인덱스
        if odd_max <= arr[j]:
            odd_max = arr[j]
            odd_max_idx = j
    else:  # 짝수번 인덱스
        if even_max <= arr[j]:
            even_max = arr[j]
            even_max_idx = j

if arr[even_max_idx - 1] < arr[even_max_idx + 1]:
    x = arr[even_max_idx + 1] - arr[even_max_idx - 1]
else:
    x = arr[even_max_idx - 1] - arr[even_max_idx + 1]

if arr[odd_max_idx - 1] < arr[odd_max_idx + 1]:
    y = arr[odd_max_idx + 1] - arr[odd_max_idx - 1]
else:
    y = arr[odd_max_idx - 1] - arr[odd_max_idx + 1]

result = ((even_max * odd_max) - (x * y))* K

print(result)

# 총평 : 열린 눈으로 규칙찾기... 가장 긴 두 변에 집중하는 아이디어는 같았지만 인접한 두 변의 길이를 뺀다는 아이디어는 도출하지 못함