function solution(answers) {
    var answer = [];
    const arr = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    let bucket = [[0, 1], [0, 2], [0, 3]]
    const len = answers.length;
    for (let i =0; i<len; i++){
        for (let j =0; j<3; j++){
            if (arr[j][i % arr[j].length] === answers[i]){
                bucket[j][0]++;
            };
        };
    };
    bucket.sort(function(a, b){
        if (a[0] === b[0]){
            return 0;
        } else {
            if (a[0] < b[0]){
                return 1;
            } else {
                return -1;
            }
        }
    });
    const max_value = bucket[0][0];
    answer = bucket.reduce((newBucket, arr) => {
        if (arr[0] === max_value){
            newBucket.push(arr[1]);
        }
        return newBucket;
    }, [])
    return answer;
}

solution([1, 3, 2, 4, 2])
