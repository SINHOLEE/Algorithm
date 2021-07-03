import heapq
def file_size(n,arr):
    total = 0
    heapq.heapify(arr)

    while len(arr)!=1:
        a=b=0
        if arr:
            a = heapq.heappop(arr)
        if arr:
            b = heapq.heappop(arr)
        heapq.heappush(arr,a+b)
        total+=(a+b )       
    return total


if __name__ == "__main__":
    k = int(input())
    for _ in range(k):
        print(file_size(int(input()),list(map(int,input().split(" ")))))
