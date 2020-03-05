# 북 동 남 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

m, n = map(int, input().split())

robot_n, commend_n = map(int, input().split())
DEBUG = True
robots = []
for _ in range(robot_n):
    x, y, d = map(str, input().split())
    if d == 'N':
        d = 2
    elif d == 'E':
        d = 1
    elif d == 'S':
        d = 0
    else:
        d = 3
    x, y = int(x), int(y)
    robots.append([y - 1, x - 1, d])
stop = True
for _ in range(commend_n):
    robot, commend, action = map(str, input().split())
    robot, action = int(robot), int(action)
    if DEBUG:
        print()
        print(robot, action, commend)
    if commend == 'F':
        for a in range(action):
            x, y, d = robots[robot - 1][0], robots[robot - 1][1], robots[robot - 1][2]
            new_x, new_y = x + di[d], y + dj[d]
            if DEBUG:
                print(x,y,d)
                print('new', new_x, new_y)
            if 0 <= new_x < n and 0 <= new_y < m:
                flag = False
                for kk in range(robot_n):
                    xx, yy, dddd = robots[kk][0], robots[kk][1], robots[kk][2]
                    if xx == new_x and yy == new_y:
                        print('Robot %s crashes into robot %s' % (robot, kk + 1))
                        stop = False
                        flag = True
                        break
                if flag:
                    break

                robots[robot - 1] = [new_x, new_y, d]
            else:
                print('Robot %s crashes into the wall' % (robot))
                stop = False
                break
    elif commend == 'R':
        robots[robot - 1][2] = (robots[robot - 1][2] - action) % 4
    else:
        robots[robot - 1][2] = (robots[robot - 1][2] + action) % 4
    if stop == False:
        break

if stop:
    print('OK')