const arr1 = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 10 ]
const arr2 = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
// https://school.programmers.co.kr/learn/courses/30/lessons/118667
// 12:55
// 힌트 봄 - 투포인터

const _sum = (a,b)=>a+b
const sum = (arr)=>arr.reduce(_sum,0)

function solution(queue1, queue2) {
    const newQueue = queue1.concat(queue2)
    let i = 0
    let j = queue1.length -1
    let cnt = 0
    const mid =sum(newQueue) / 2
    let cur = sum(queue1)
    while (cnt <= (queue1.length) * 3){
        if(cur===mid){
            return cnt
        } else if (cur>mid){
            cur -= newQueue[i]
            i = (i + 1) % newQueue.length
        }else{

            j = (j + 1) % newQueue.length
            cur += newQueue[j]

        }
        cnt++

    }
    return -1;
}

console.log(solution(arr2,arr1))