class node():
    def __init__(self, data, link):
        self.data = data
        self.link = link

    #
    # def __str__(self):  # 객체의 내부정보를 문자열로 반환, 디버깅용
    #     return 'data = {}, link = {}'.format(self.data, self.link)


    def __repr__(self): # JSON 문자열로 반환, JSON.prase()로 복구하기 위한 문자열
        return '{"data" : %s, "link" : %s }'


n1 = node(100, None)

print(n1    )