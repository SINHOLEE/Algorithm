def _is_contain_seven(n):
    if n == 0:
        return False
    if n % 10 == 7:
        return True
    return _is_contain_seven(n // 10)


def _is_divided_seven(n):
    if n % 7 == 0:
        return True
    else:
        return False


def _check_seven(n):
    return True if (_is_divided_seven(n) or _is_contain_seven(n)) else False


def _solution(n, data):
    if n == 1:
        return 1
    if _is_divided_seven(n-1) or _is_contain_seven(n-1):
        return _solution(n-1, data * -1) + data
    else:
        return _solution(n-1, data) + data


# 시작할 때 -1로 시작할지, +1로 시작할지 판단을 위한 함수
# 즉 방향전환을 홀수만큼 했다면 _solution(n,data)에서의 data가 -1로 시작해야 재귀의 base case인 n == 1일때 data가 1이 되므로
def _check_start(n):
    if n == 1:
        return 0
    if _check_seven(n-1):
        return _check_start(n - 1) + 1
    else:
        return _check_start(n - 1)


# 해당방식은 O(n)의 복잡도를 가지고 있지만  maximum recursion depth exceeded 오류로 n이 996이상은 검사하지 못하는 단점이 있다.
def ping_pong(n):
    return _solution(n, -1 if _check_start(n) % 2 else 1)


for i in range(1, 996):
    print(i, ping_pong(i))
