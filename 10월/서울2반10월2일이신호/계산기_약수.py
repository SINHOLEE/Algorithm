# 약수들의 집합을 만드는 함수
def div(n, temp):
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            temp.append(i)
            temp.append(n // i)
    return sorted(temp)

# 버튼만 사용해서 함수의 인자를 만들 수 있는지 판단하는 함수, 만약 만들 수 있으면 숫자를, 없으면 False를 반환한다.
def check_able(n):
    count = 0
    while True:
        if n == 0:
            return count
        temp = n % 10
        flag = True
        for i in my_nums:
            if i == temp:
                count += 1
                flag = False
                break
        n = n // 10
        if flag:
            return False

# 버튼을 이용해서 만들 수 있는 숫자와 그 숫자를 만들 때 버튼을 누르는 최소값을 저장하는 디피를 만드는 함수, 두번째 인자는 디버깅용으로 삽인한 것으로 사용할 필요 없다.
def make_dp(divisors, dp):
    c = len(divisors)
    if c == 0:  # divisors의 길이가가 0이라면 더이상 쪼개지지 않는다는 뜻이므로 위의 반복을 그만둔다.
        return

    # divisors는  div(숫자)를 뜻한다. 즉 내가 궁금한 숫자의 약수들을 담은 리스트이다.
    for num in divisors:  # 각각의 약수를 체크
        temp_chk = check_able(num)  #이 함수가 숫자를 반환하면, 내가 계속 봐왔던 약수가 버튼만으로 누를 수 있다는 뜻
        if temp_chk:  # 약수가 버튼만으로 만들 수 있다면
            if num not in dp:  # 만약 dp dict안에 해당 약수가 key인 원소가 없다면 처음 접한 숫자이므로
                dp[num] = temp_chk  # 해당 숫자를 key값으로, 해당 숫자를 만들 때 누르는 버튼의 횟수를 value값으로 저장한다.

            # else:  # 만약 dp안에 해당 약수가 있다면 혹시나 해서 조건을 부여했지만 결론적으론 필요 없다.
            #     if dp[num] > temp_chk:
            #         dp[num] = temp_chk

        else:  # 약수가 버튼만으로 만들 수 없다면, 해당 수를 위의 과정을 반복하여 더 이상 나눌 수 없는 서로소단위까지 쪼개어 dp에 저장한다.
            make_dp(div(num, []), dp)


    for k in range(c // 2 + 1):  # 현재 약수들의 최소 생성 횟수를 저장한 dp를 이용하여 dp를 최신화 한다.
        a = dp.get(divisors[k])
        b = dp.get(num // divisors[k])

        if a != None and b != None:
            if num not in dp:
                dp[num] = a + b + 1
            else:
                if dp[num] > a + b + 1:
                    dp[num] = a + b + 1
T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    target = int(input())
    len_nums = len(nums)
    my_nums = []
    for idx in range(len(nums)):
        if nums[idx]:
            my_nums.append(idx)
    # print(target)
    # print(my_nums)
    if target == 1:
        print('#%s 2' % tc)
        continue
    frist = check_able(target)
    if frist:
        print('#%s %s' % (tc, frist+1))
        continue
    else:
        dp = {}
        my_div = div(target, [])
        make_dp(my_div, dp)

        if dp == dict():
            print('#%s -1' % tc)
        else:
            # print(dp)
            my_min = 999999999
            c = len(my_div)
            for i in range(c // 2 + 1):
                a = dp.get(my_div[i])
                b = dp.get( target // my_div[i])
                if a != None and b != None:
                    temp = a + b + 2
                    if my_min > temp:
                        my_min = temp
            if my_min == 999999999:
                print('#%s -1' % tc)
            else:
                print('#%s %s' % (tc, my_min))
