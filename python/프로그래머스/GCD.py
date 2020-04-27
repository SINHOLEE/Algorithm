def GCD(a, b):
    max_value = max(a, b)
    min_value = min(a, b)
    moduled = max_value % min_value

    if moduled == 0:
        return min_value

    return GCD(min_value, moduled)


print(GCD(1112, 695))
