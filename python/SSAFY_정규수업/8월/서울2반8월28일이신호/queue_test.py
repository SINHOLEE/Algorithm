my_que = [0] * 1000

# enQueue
top = -1
tail = -1
# enQueue
tail += 1
my_que[tail] = 10
# enQueue
tail += 1
my_que[tail] = 20

#deQueue
top += 1
my_que[top] = 0

#deQueue
top += 1
my_que[top] = 0

# isEmpty
def isEmpty(top, tail):
    if top == tail:
        return True
    else:
        return False

print(my_que)
print(top, tail)

print(isEmpty(top, tail))