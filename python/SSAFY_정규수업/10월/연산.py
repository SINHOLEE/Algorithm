from collections import deque


T = int(input())

for tc in range(1, T+1):
    start, target = map(int, input().split())
    my_queue = deque([start])
    visited = set()
    visited.add(start)
    count = 0
    flag = False
    while True:
        if flag:
            break

        for i in range(len(my_queue)):
            result = my_queue.popleft()
            if result == target:
                flag = True
                break

            for num in range(4):
                if num == 0:
                    new = result + 1
                elif num == 1:
                    new = result - 1
                elif num == 2:
                    new = result * 2
                else:
                    new = result - 10
                if new > 1000000:
                    continue
                if new in visited:
                    continue
                if new == target:
                    flag = True
                    break
                my_queue.append(new)
                visited.add(new)

        count += 1

    print('#%s %s' % (tc, count))
