
const add = function(num1, num2){
    return num1 + num2
}


const sub = function(num1, num2){
    return num1 - num2
}

const solution = function(arr) { 
    if (arr.length === 1){
        return arr[0]
    }else {
        if (arr[1] === '+'){
            return solution([add(arr[0], arr[2])].concat(arr.slice(3)))
        } else {
            return solution([sub(arr[0], arr[2])].concat(arr.slice(3)))
        }
    }
}


// 1 + 2 + 3 - 4 = ?
console.log(solution([1, '+',  2, '-', 3]))


// 계산기 