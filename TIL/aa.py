for t in range(1, int(input()) + 1):
    num = str(input())
    a = ""
    b = ""
    for n in num:
        if n == "4":
            a += "3"
            b += "1"
        else:
            a += n
            b += "0"

    print("Case #1: %s %s" % (int(a), int(b)))

