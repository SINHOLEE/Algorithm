def c(l,r):
    return int((l + r)/2)

class book:
    def __init__(self, l, r, p):
        self.l = l
        self.r = r
        self.p = p
        self.c = c(self.l, self.r)
        self.count = 0
        self.stop = 0

    def serch(self):
        if  self.c < self.p:
            self.l = self.c
            self.count += 1
            self.c = c(self.l, self.r)
        elif self.c > self.p:
            self.r = self.c
            self.count += 1
            self.c = c(self.l, self.r)
        else:
            self.stop = 1

def whoswinner(r, pa, pb):
    l = 1
    a = book(l, r, pa)
    b = book(l, r, pb)
    while (True) :
        
        if a.stop == 1 and b.stop == 1:
            break

        else:              
            a.serch()
            b.serch()
            
    if a.count < b.count:
        result = 'A'
    elif a.count > b.count:
        result = 'B'
    else:
        result = 0  
    return result

T = int(input())

for tc in range(1, T+1):
    r ,pa, pb = input().split()
    r, pa, pb = int(r), int(pa), int(pb)

    print('#{} {}'.format(tc, whoswinner(r, pa, pb)))

