sticker = [12, 80, 14, 22, 100]
def fn(depth,index, sum_of_stickers, sum_of_others, visited,my_lis):
    global answer,  len_of_sticker



def solution(sticker):
    global answer, visited, len_of_sticker
    answer = 0

    len_of_sticker = len(sticker)
    my_list = [0] * len_of_sticker
    visited = [False] * len(sticker)
    fn(0, 0, 0, sum(sticker), visited,my_list)

    return answer

print(solution(sticker))