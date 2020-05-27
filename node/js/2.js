function solution(arr) {
    const my_set = new Set();
    for(let i=0; i<arr.length; i++){
        let temp = arr[i].toString();
        temp = temp.split('').sort().toString();
        my_set.add(temp);
    }

    return my_set.size;
}

console.log(true,solution([112, 1814, 121, 1481, 1184]))
