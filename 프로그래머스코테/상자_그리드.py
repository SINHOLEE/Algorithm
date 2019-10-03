goods = [5,3,7]
boxes = [3,7,6]

def solution(goods, boxes):
    answer = 0
    goods = sorted(goods, reverse = True)
    boxes = sorted(boxes, reverse = True)
    boxes_index = 0
    boxes_len = len(boxes)
    for item_size in goods:
        if boxes_index == boxes_len:
            break
        if item_size <= boxes[boxes_index]:
            answer += 1
            boxes_index+=1

    return answer

print(solution(goods,boxes))