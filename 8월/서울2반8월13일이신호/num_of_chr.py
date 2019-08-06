T = int(input())

def my_max(a_list):
    mx = 0
    for a in a_list:
          if a > mx:
              mx = a
    return mx

for tc in range(1, T+1):
    first = input()
    second = input()


    temp = []
    for f_chr in first:
        count = 0
        for s_chr in second:
            if f_chr == s_chr:
                count += 1
        temp += [count]

    print('#{} {}'.format(tc, my_max(temp)))