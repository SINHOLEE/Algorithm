def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    point = 1
    answer = 0
    bucket = [""] * cacheSize
    for city in cities:
        temp = city.lower()

        if temp in bucket:
            answer += 1
            for i in range(cacheSize):
                if temp == bucket[i]:
                    bucket.pop(i)
                    break
        else:
            answer += 5
            bucket.pop(0)
        bucket.append(temp)
    return answer

