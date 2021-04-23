def main(n,m,arr):
    answer = 0
    s= 0
    e = 1000000000

    while s<=e:
        mid = (s+e)//2
        total_woods = sum(map(lambda x: x-mid if x>mid else 0,arr ))
        if total_woods < m:
            e=mid-1
        else:
            answer = mid
            s=mid+1
    return answer

if __name__ == '__main__':
    n,m = map(int, input().split(" "))
    arr = [*map(int, input().split(" "))]
    print(main(n,m,arr))
    # print(n,m,arr)
    # print(main(4,7,[20,15,10,17]))