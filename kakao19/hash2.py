phone_book = 	["123", "456", "789"]

def solution(phone_book):
    #nC2 기본
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):

            # 둘 중 길이가 작은 애들을 기준으로 서로 비교하기
            if len(phone_book[i]) > len(phone_book[j]):
                if phone_book[i][:len(phone_book[j])] == phone_book[j]:
                    return False
            else:
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    return False
    #여기까지 왔는데 같은게 없으면 트루반환
    return True



print(solution(phone_book))