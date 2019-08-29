
def batte(a, b):
    # 만약 a랑 b가 비기면
    if cards[a] == cards[b]:
        # a가 앞 인덱스므로 a가 이겼다고 생각하자
        return a

    # 만약 a랑 b가 비기지 않는다면,
    else:
        # 가위와 보가 숫자로 보면 보가 이기지만 실제로는 가위가 이기므로 예외처리한다.
        if cards[a] == 1 and cards[b] == 3:
            return a
        elif cards[a] == 3 and cards[b] == 1:
            return b
        else:
            if cards[a] > cards[b]:
                return a
            else:
                return b


def tournament(li, start, end):
    # 계속 쪼개다가 하나만 남으면 리턴
    if start == end:
        return start
    # 절반지점 
    p = (start + end) // 2

    a = tournament(li, start, p)
    b = tournament(li, p + 1, end)
    # result에서 반환하는 값은 a와 b 중 이긴 index값을 반환 결국 되돌아오면 최종승자의 인덱스 반환
    result = batte(a, b)

    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, tournament(cards, 0, len(cards) - 1) + 1))