//https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=javascript

// 4:25

// 0,0 h-1, w-1
// h = routes.length
// w = routes[0].length
// start 좌표 찾기
// init: 동, 서, 남, 북 매핑
//
const findCurrentPos = (board)=>{
    for(let i = 0; i<board.length; i++){
        for (let j=0; j<board[0].length; j++){
            const current = board[i][j]
            if(current === 1){
                return [i, j]
            }
        }
    }}
const createBoardByPark = (park)=>{
// 0 빈칸
// 1 현재위치
// 2 장애물
    const board = []
    for(let i = 0; i<park.length; i++){
        // 실수 1 Array(park.length).fill(0) 로 함
        const row = Array(park[i].length).fill(0)
        for (let j=0; j<park[0].length; j++){
            const current = park[i][j]
            if(current === 'S'){
                row[j] = 1
            }
            if(current === 'O'){
                row[j] = 0         }
            if(current === 'X'){
                row[j] = 2         }
        }
        board.push(row)
    }
    return board
}

const DIRECTION = {
    'N':[-1,0],
    'S':[1,0],
    'W':[0,-1],
    'E':[0,1]
}

const parseRoute = ( route) =>{
    const parsedRoute = route.split(' ')
    const dir = parsedRoute[0]
    const distance = parseInt(parsedRoute[1],10)

    return {dir,distance}
}
const createNewPos = ([currentY,currentX],route)=>{
    const {dir, distance } = parseRoute(route)
    return [currentY+DIRECTION[dir][0]*distance,currentX+DIRECTION[dir][1] * distance ]
}

const hasXInPath = ([currentY,currentX], route, board)=>{
    const {dir, distance } = parseRoute(route)
    let round = 0
    // 실수2 (distance+1) 안하고 distance 만 함
    while (round !== (distance+1)){
        const newY = currentY + DIRECTION[dir][0] * round
        const newX = currentX + DIRECTION[dir][1] * round

        if(board[newY][newX]===2){
            return true
        }
        round += 1
    }
    return false


}

const canMove=(currentPos,route,board)=>{
    const [newY,newX] = createNewPos(currentPos,route)
    // 보드보다 넘어가는지?
    if(newY<0 || newY > board.length-1 || newX<0 ||newX>board[0].length-1){

        return false
    }
    if(hasXInPath(currentPos, route, board)){

        return false
    }
    return true
}
function solution(park, routes) {
    const board = createBoardByPark(park)
    let currentPos = findCurrentPos(board)
    for (const route of routes){
        if(!canMove(currentPos,route,board))continue
        const newPos = createNewPos(currentPos,route)
        board[currentPos[0]][currentPos[1]] = 0
        board[newPos[0]][newPos[1]] = 1
        currentPos = newPos


    }

    return currentPos;
}

/**
 * 입출력
 *     park                    routes                 result
 *     ["SOO","OOO","OOO"]    ["E 2","S 2","W 1"]    [2,1]
 *     ["SOO","OXX","OOO"]    ["E 2","S 2","W 1"]    [0,1]
 *     ["OSO","OOO","OXO","OOO"]    ["E 2","S 3","W 1"]    [0,0]
 *
 */

