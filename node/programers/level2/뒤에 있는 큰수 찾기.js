// https://school.programmers.co.kr/learn/courses/30/lessons/154539

// 3:25
function solution(numbers) {
    const stack = []
    const answer = Array(numbers.length).fill(0)
    for (let tail = numbers.length - 1; tail >= 0; tail--) {
        if (stack.length === 0) {
            answer[tail] = -1
        } else {
            while (stack.length) {
                const num = stack.pop()
                if (num > numbers[tail]) {
                    answer[tail] = num
                    stack.push(num)
                    break
                } else if (stack.length === 0) {
                    answer[tail] = -1
                }
            }
        }


        const num = numbers.pop()
        stack.push(num)

    }


    return answer;
}
