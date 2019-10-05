T = int(input())
def DFS(squre,  width, height, depth, current_boxes):
    global min_area
    if depth == 3:
        if min_area > (width * height):
            min_area = (width * height)
        return
    if min_area < width * height:
        return
    for i in range(3):
        if visited[i] == False:
            visited[i] = True
            DFS(boxes[i], width+boxes[i][0], max(height, boxes[i][1]), depth+1, current_boxes+[boxes[i]])
            DFS(boxes[i], width+boxes[i][1], max(height, boxes[i][0]), depth+1, current_boxes+[boxes[i]])
            DFS(boxes[i], max(width , boxes[i][0]), height+boxes[i][1], depth + 1, current_boxes + [boxes[i]])
            DFS(boxes[i], max(width, boxes[i][1]), height + boxes[i][0], depth + 1, current_boxes + [boxes[i]])
            visited[i] = False
for tc in range(T):
    boxes = []
    for _ in range(3):
        boxes.append(tuple(map(int, input().split())))
    visited = [False] * 3
    min_area = 99999999
    for idx in range(3):
        visited[idx] = True
        DFS(boxes[idx], boxes[idx][0], boxes[idx][1] ,1, [boxes[idx]])
        visited[idx] = False
    print(min_area)