def _is_contain_seven(n):
    if n == 0:
        return False
    return True \
        if n % 10 == 7 \
        else _is_contain_seven(n // 10)


def _is_divided_seven(n):
    return False if n % 7 else True


def _check_seven(n):
    return True \
        if (_is_divided_seven(n) or _is_contain_seven(n)) \
        else False


def _solution(n, data):
    if n == 1:
        return 1
    return _solution(n-1, data * -1) + data \
        if _check_seven(n-1) \
        else _solution(n-1, data) + data


def _check_start(n):
    if n == 1:
        return 0
    return _check_start(n - 1) + 1 \
        if _check_seven(n-1) \
        else _check_start(n - 1)


def ping_pong(n):
    return _solution(n, -1 if _check_start(n) % 2 else 1)


print(ping_pong(996))