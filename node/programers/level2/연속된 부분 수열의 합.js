//https://school.programmers.co.kr/learn/courses/30/lessons/178870
//4:55 검증 20분 코드20분
function solution(sequence, k) {
    let s = 0
    let e = 0
    let acc = sequence[0]
    let res = [0, sequence.length-1]
    let size = sequence.length
    while(e<sequence.length){
        if(acc===k){
            const curSize = e-s+1
            if(curSize<size ||(curSize===size&&s<res[0])){
                size = curSize
                res = [s,e]
            }
        }
        if(acc <= k){
            e+=1
            acc+=sequence[e]
        }else{
            acc-=sequence[s]
            s+=1
        }
    }
    return res;
}