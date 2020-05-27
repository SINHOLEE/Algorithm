function recursive(arr, cnt){
    answer = Math.max(answer, cnt);
    if (arr.length === 1){
        return
    }
    for (let i = 0; i<arr.length-1; i++){
        for(let j = i+1; j<arr.length; j++){
            if(arr[i][0] === arr[j][0]){
                const new_arr = [[arr[i][0] + arr[j][0], arr[i][1]+arr[j][1]]].concat(arr.slice(1));
                console.log(new_arr);
                recursive(new_arr, arr[i][1]+arr[j][1]);
            } else if (arr[i][0] < arr[j][0]){
                continue
            } else {
                continue;
            }
        }
    }
};

function solution(weights){
    weights.sort(function(a, b) {
        return parseInt(a) - parseInt(b); 
    });

    weights = weights.reduce((prev, curr) => {
        prev.push([parseInt(curr), 1]);
        return prev;
    },[])
    console.log(weights);
    recursive(weights, 0);
    console.log(answer);
    return answer;
}

let answer = 0;
solution([16, 16, 16, 16, 16, 16, 16, 16, 1, 1, 2, 4, 4])