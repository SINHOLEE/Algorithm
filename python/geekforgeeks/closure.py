def in_cache(func):
    cache = {}
    def wrapper(n):
        print(cache) ## !!!!
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return wrapper


def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret


def sum_to_N(N):
    s = 0
    for n in range(N+1):
        s += n
    return s



factorial = in_cache(factorial)

sum_to_N = in_cache(sum_to_N)

factorial(10)
factorial(10)
sum_to_N(10)
sum_to_N(10)
