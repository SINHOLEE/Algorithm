function solution(arr) {
    var answer = true;
    arr.sort();
    console.log(arr);
    let temp = 1;
    console.log(arr.length);
    for (let i = 0; i<arr.length; i++){
        if (i+1 !== arr[i]) {
            answer = false;
            break
        }
    }
    return answer;
}

console.log(true,solution([]))
