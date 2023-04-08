// https://school.programmers.co.kr/learn/courses/30/lessons/169199
//1:55->40분 씀...
// 멈춰진곳에서 이동할 방향을 체크
// 큐에 저장은 멈춰진 위치의 좌표와, 현재까지 이동거리 저장
// 큐에서 shift 된 값의 위치가  g라면 cnt를 return
// 아니라면 4방향으로 갈 준비함
//      이때 이미 같은위치에 같은방향으로 갔던 경험이 있으면 queue에 담지 않음
//      갔던 경험이 없으면 queue에담고 visited에 방향에 대한 정보 추가
// 반복해서 return 안되면 -1 리턴
const dy = [0,0,1,-1]
const dx = [1,-1,0,0]

const isOutBound = (y,x,height,width) =>{
    return y<0 || y>=height || x<0 ||x>=width
}

const getNewPosition = (y,x,direction,board)=>{
    let yy = y
    let xx = x
    while(!isOutBound(yy+dy[direction],xx+dx[direction],board.length,board[0].length) && board[yy+dy[direction]][xx+dx[direction]] !== 'D'){
        yy+=dy[direction]
        xx+=dx[direction]
    }
    return [yy, xx]

}
const findStartPos = (board)=>{
    for ( let i = 0; i<board.length; i++){
        for ( let j = 0; j<board[0].length; j++){
            if(board[i][j]==='R'){
                return [i,j]
            }
        }
    }

}

const createVisited = (board)=>{
    const visited = []

    for ( let i = 0; i<board.length; i++){
        const temp = []
        for ( let j = 0; j<board[0].length; j++){
            temp.push([false,false,false,false])
        }
        visited.push(temp)
    }
    return visited
}



function solution(board) {
    let res = 0
    const visited = createVisited(board)
    const [y,x] = findStartPos(board)
    const queue = []

    // visited 조작 & queue 조작
    for(let d =0; d<4; d++){
        const [yy,xx] = getNewPosition(y,x,d,board)
        if(yy===y && xx===x) continue
        visited[y][x][d] = true
        queue.push([yy,xx,1])
    }

    // bfs 탐색
    while(queue.length){
        const [y,x,cnt] = queue.shift()
        if(board[y][x]==='G'){
            return cnt
        }
        for(let d =0; d<4; d++){
            const [yy,xx] = getNewPosition(y,x,d,board)
            if(yy===y && xx===x) continue
            if(visited[y][x][d]) continue
            visited[y][x][d] = true
            queue.push([yy,xx,cnt+1])
        }

    }
    return -1;
}