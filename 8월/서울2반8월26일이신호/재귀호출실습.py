n = 3 + 2 + 1


def mysum(num):
    if num == 1:
        return 1

    else:
        return num + mysum(num - 1)
print(mysum(10))