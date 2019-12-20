import time

class my_random:
    def __init__(self, n):
        self.n = n
        self.my_list = [ i for i in range(n) for _ in range(n)]

    def show(self):
        a = self.my_list.pop(0)
        mid = int(time.time()*1000) % self.n
        self.my_list += [a]
        self.my_list = self.my_list[mid:] + self.my_list[:mid]

        return a

rand5 = my_random(5)


def rand7():
    while True:
        n = (rand5.show()) * 5 + rand5.show()+1
        if n < 21:
            return n // 3



cnt = 0
my_cnt = [0] * 7
while cnt != 50000:
    my_cnt[rand7()] += 1
    cnt+=1

print(my_cnt)

# print(random.show())
# print(random.show())
# print(random.show())
# print(random.show())
# print(random.show())
