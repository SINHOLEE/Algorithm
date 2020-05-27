function recursive(arr, cnt){
    if (arr.length === 1 && arr[0] === 1){
        return cnt;
    } else{
        let new_arr = [];
        let prev = arr[0];
        let cn = 0;
        for(let i = 0; i<arr.length; i++){
            if(prev === arr[i]){
                cn++;
            } else {
                prev = arr[i];
                new_arr.push(cn);
                cn = 1;
            }
        }
        if (cn){
            new_arr.push(cn);
        }
        cnt = recursive(new_arr, cnt + 1);
        console.log(new_arr, cnt);
        return cnt
    }
}

function solution(arr) {
    return recursive(arr, 0);
}

console.log(true,solution([1,3]))
