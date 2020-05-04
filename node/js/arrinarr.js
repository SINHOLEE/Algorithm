const n = 3;
const m = 5;

let arr = Array.from(Array(n), ()=>Array(m));
let c = 1;

for (let i = 0; i < 3; i++){
    for (let j = 0; j < 5; j++){
        arr[i][j] = c;
        c++;
    }
    console.log(arr[i])
}

console.log(arr)

/*
[ 1, 2, 3, 4, 5 ]
[ 6, 7, 8, 9, 10 ]
[ 11, 12, 13, 14, 15 ]
*/