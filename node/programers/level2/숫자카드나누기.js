//2:22
// arrayA와 arrayB에서 제일 큰 숫자를 각각 뽑는다.
// 1. arrayA 먼저
// 제일 큰 숫자의 약수배열을 모은다.
// 배열을 순회하면서 조건에 맞는 값을 찾는다.
// 2. arrayB를 1과 같이 돌린다.


// 런타임에러가 나왔던 이유
// Math.max(...arr) 에서 500000개의 원소를 커버하지 못한다.
// Uncaught RangeError: Maximum call stack size exceeded 런타임 에러가 발생함.

const createGCDList = (target) => {
    const subs = []
    for (let i = 1; i < Math.floor(Math.sqrt(target)) + 1; i++) {
        if (target % i === 0) {
            subs.push(i)
            subs.push(Math.floor(target / i))
        }
    }
    return subs
}

const findMax = (arr) => {
    let ans = 0
    for (const num of arr) {
        ans = Math.max(ans, num)
    }
    return ans
}

const calcAnswer = (gcdList, arr1, arr2) => {
    let ans = 0
    for (const sub of gcdList) {
        if (arr1.every(num => num % sub === 0) && arr2.every(num => num % sub !== 0)) {
            ans = Math.max(ans, sub)
        }
        if (arr2.every(num => num % sub === 0) && arr1.every(num => num % sub !== 0)) {
            ans = Math.max(ans, sub)
        }
    }
    return ans
}

function solution(arrayA, arrayB) {
    const maxA = findMax(arrayA)
    const maxB = findMax(arrayB)

    const GCDListA = createGCDList(maxA)
    const GCDListB = createGCDList(maxB)


    return Math.max(
        calcAnswer(GCDListA, arrayA, arrayB),
        calcAnswer(GCDListB, arrayA, arrayB),
    );
}