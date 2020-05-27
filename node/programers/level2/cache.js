function solution(cacheSize, cities) {
    var answer = 0;
    cities = cities.map(el=>el.toLowerCase())
    let cache = new Array();
    cities.forEach(element => {
        if (cache.includes(element)){  // 포함하면 그 값 지우고 그 값 푸시
            cache = cache.reduce((prev, curr)=> {
                if (curr !== element) {
                    prev.push(curr);
                }
                return prev;
            }, []);
            cache.push(element);
            answer++;
        } else {
            if (cache.length === cacheSize){
                cache.shift();  // 하나도 없지 않으면 뺀다.
            }
            if (cacheSize > 0){
                cache.push(element);
            }
            answer += 5;

        }
    });
    return answer;
}

// console.log(50,solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) );
// console.log(21, solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
// console.log(60, solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]));
// console.log(52, solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]));
console.log(16, solution(	0, ["Jeju", "Pangyo", "NewYork", "newyork"]));
// console.log(25, solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))