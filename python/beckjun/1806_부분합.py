def main(N,target,arr):
    # e의 끝은 N이다.
    # e가 N보다 커지면 멈춘다
    # s가 e와 같으면 멈춘다...? 가능한 조건인가? ㅇㅇ s가 하나의 item보다 작다면 가능
    # target보다 부분합이 크거나 같으면  1) 현재 개수 구하고(e-s) 2)s++
    # target보다 부분합이 작으면 e++
    if sum(arr)< target:
        return 0
    s= 0
    e = 1
    sub_sum = arr[0]
    answer = 9999999
    while e<=N:
        if sub_sum >= target:
            answer = min((e-s),answer)
            sub_sum -= arr[s]
            s+=1
        else:
            if(e!=N):
                sub_sum += arr[e]
            e+=1
    return 0 if answer==9999999 else answer


if __name__ == '__main__':
    N,S = map(int,input().split(" "))
    arr = [*map(int, input().split(" "))]
    print(main(N,S,arr))
    
    print(main(10,15,[5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
    