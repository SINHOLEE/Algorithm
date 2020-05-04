const arr = ['a', 'b', 'f', 'd', 'c', 'a']

arr.sort(function(a, b){
    return b.charCodeAt() - a.charCodeAt();
})

console.log(arr)


// console.log('a'.charCodeAt() - 's'.charCodeAt())