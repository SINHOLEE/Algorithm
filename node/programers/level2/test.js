// const obj = {'a': 1, 'b':2, 'c':3};
// for (const[key, value] of Object.entries(obj)) {
//     console.log(key, value);
// };


// console.log(String.fromCharCode(97));

let mat = [[1,0,0,0],
[1,1,1,0],
[0,0,1,0],
[0,1,0,0]];


let temp = mat[0][0];
mat[0][0] = mat[0][1];
mat[0][1] = temp;

console.log(mat);
