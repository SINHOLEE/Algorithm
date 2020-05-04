function solution(clothes) {
    var answer = 1;
    const dic = clothes.reduce((obj, clothe) => {
        if (obj[clothe[1]]){
            obj[clothe[1]]+=1
        } else {
            obj[clothe[1]] = 1
        }
        return obj;
    }, {})

    for (const [key, value] of Object.entries(dic)){
        answer *= value+1
    }
    return answer - 1;
}


solution(	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
)