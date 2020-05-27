function solution(n)
{
    var answer = 0;
    while (n !== 0){
        answer += n % 10;
        n = parseInt(n / 10);
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer;
}
console.log(solution(123))