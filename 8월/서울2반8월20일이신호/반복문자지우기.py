T = int(input())

for tc in range(1, T+1):
    string = input()
    string += '#'
    count = 0
    while count != len(string)-1 and len(string) != 0:
        count = 0
        for chr in range(0, len(string) - 1):
            if string[chr] == string[chr+1]:
                string = string[:chr]+string[chr+2:]
                break
            else:
                count += 1

    print('#{} {}'.format(tc, len(string) - 1))
