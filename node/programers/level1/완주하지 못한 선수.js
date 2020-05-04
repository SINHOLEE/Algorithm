function solution(participant, completion) {
    let map = {};
    var answer = '';
    let com = "";
    let prt = "";
    
    for (com of completion){
        if (map[com] === undefined){
            map[com] = 1
        } else {
            map[com] += 1
        }
    };
    for (prt of participant) {
        map[prt] -= 1
    };

    for (const obj in map){
        if (map[obj] !== 0){
            answer = obj;
            break;
        }
    };
    return answer;
}


solution(	["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
