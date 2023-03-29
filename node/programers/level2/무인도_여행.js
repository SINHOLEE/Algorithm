
// https://school.programmers.co.kr/learn/courses/30/lessons/154540
// 4:30 ->4:50 ->5:20
// 왜 시간을 이렇게 많이썻나? sort 기본 동작이 string 이란걸 까먹었다.
//    return answer.length? answer.sort((a, b) => a - b):[-1]; 이렇게 안하고
//     return answer.length? answer.sort():[-1]; 이렇게 해서 문제였음

const dy = [0,0,-1,1]
const dx = [-1,1,0,0]

const isOutBound = (y,x,maps)=>{
    return x < 0 || x >= (maps[0].length) || y < 0 || y >= maps.length
}

const canGo = (y,x,maps,visited)=>{
    return !isOutBound(y,x,maps) &&  visited[y][x] === 0 && maps[y][x] !== 'X'
}

const createEmptyVisited = (maps)=>{
    const visited = []
    for(let i =0; i<maps.length; i++){
        const row = Array(maps[i].length).fill(0)
        visited.push(row)
    }

    return visited
}
// dfs
const calcTotalStayDuration = (i,j,visited,maps)=>{
    const stack = [[i,j]]
    let acc = 0
    visited[i][j] = 1

    while(stack.length){
        const [y,x] = stack.pop()
        acc+=parseInt(maps[y][x],10)

        for(let dIndex=0; dIndex<4;dIndex++){
            const ny = y + dy[dIndex]
            const nx = x + dx[dIndex]
            if (!canGo(ny,nx,maps,visited)) continue

            visited[ny][nx] = 1
            stack.push([ny,nx])

        }
    }
    return acc
}
function solution(maps) {
    const visited =createEmptyVisited(maps)
    const answer = [];


    for ( let i = 0; i<maps.length; i++){
        for(let j = 0; j < maps[i].length; j++){

            if(!canGo(i,j,maps,visited)) continue
            const stayDuration = calcTotalStayDuration(i,j,visited,maps)
            answer.push(stayDuration)

        }
    }



    return answer.length? answer.sort((a, b) => a - b):[-1];
}