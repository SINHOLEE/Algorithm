def backtracking(station, energy, destination, cnt):
   global result_cnt
   if cnt >= result_cnt:
       return
   for i in range(station+1, station+energy+1):
       if destination <= i:
           result_cnt = cnt
           return
       backtracking(i, info[i], destination, cnt + 1)
for tc in range(1, int(input().strip()) + 1):
   info = list(map(int, input().strip().split()))
   result_cnt = info[0] - 2
   backtracking(1, info[1], info[0], 0)
   print('#%d' %(tc), result_cnt)


