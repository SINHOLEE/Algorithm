n = int(input())
arr = [*map(int, input().split())]
target = 1
side = []
for _ in range(n):
    front = arr.pop(0)
    if front == target:
        target += 1
    else:
        side.append(front)
    while side:
        if side[-1] == target:
            side.pop()
            target += 1
        else:
            break
print("Nice" if target == n+1 else "Sad")
