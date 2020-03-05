dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for t in range(1, T+1):
    n = int(input())
    atoms = {}
    cnt_atoms = n
    total_energy = 0
    for i in range(n):
        x, y, d, e = map(int, input().split())
        atoms[(x*2, y*2)] = [d,e]

    c = 0
    while cnt_atoms:
        new_atoms = {}
        visited = set()
        c+=1
        for k, lis in atoms.items(): # 내가 가지고 있는 모든 원소들을 한번씩 움직일것이다.
            x,y,d,e = k[0],k[1],lis[0],lis[1]

            xx, yy= x+dx[d], y+dy[d]

            if -2001<=xx<=2001 and -2001<=yy<=2001:
                if new_atoms.get((xx, yy)) == None:
                    new_atoms[(xx, yy)] = [d, e]
                else:
                    visited.add((xx,yy))
                    cnt_atoms-=1
                    total_energy += e
            else:
                cnt_atoms -= 1

        for x, y in visited:
            total_energy += new_atoms[(x,y)][1]
            cnt_atoms -= 1
            del(new_atoms[(x,y)])
        atoms = new_atoms


    print('#%s %s' % (t,total_energy))