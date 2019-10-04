'''
k번째 순열 찾기
예를 들어 숫자 1, 2, 3으로 만들 수 있는 순열 중 오름차순으로 정렬 했을 때 3번째 순열은 213이다.

조합된 순열	순서(오름차순)
123	1
132	2
213	3
231	4
312	5
321	6
제한 사항
순열을 조합할 때 주어진 숫자를 모두 한번씩 사용해야 한다
입력 형식
첫 번째 행에 공백(space)을 구분자로 숫자가 주어진다
각 숫자는 한 자리 숫자로 주어진다 (0과 같거나 크고, 10보다 작은 숫자)
같은 숫자가 중복되어 나타나지 않는다
두 번째 행에 찾으려는 수열의 순서(k)가 주어진다
k는 조합된 순열의 개수보다 크거나 작지 않다
출력 형식
조합된 순열을 오름차순으로 정렬 했을 때 k번째 순열
맨 앞자리가 0인 경우는 0을 그대로 유지한다

'''


# import itertools
#
# nums = list(map(int, input().strip().split(' ')))
# find_number = int(input())
# results = []
# for perm in itertools.permutations(nums):
#     results.append(perm)
# results.sort()
# for num in results[find_number-1]:
#     print(num, end='')
#
'''
1 0 2
5
'''
nums = list(map(int, input().split()))
target = int(input())
count = 0
# print(nums)
nums = sorted(nums)
result = 0
def perm(r, tem):
    global count, target,result
    if len(tem) == len(nums) and count < target:
        count += 1
        if count == target:
            result = str(''.join(map(str,tem)))
        return


    for i in range(len(nums)):
        if visited[i] == False:
            visited[i] = True
            perm(r+1, tem +[nums[i]])
            visited[i] = False
visited = [False] * len(nums)
temp = []

perm(0, temp)
print(result)