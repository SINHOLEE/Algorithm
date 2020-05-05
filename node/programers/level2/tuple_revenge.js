function solution(s) {
    let a = s.substring(2, s.length - 2).split('},{');
    console.log(a);
    a.sort((a, b) => a.length - b.length);
    console.log(a);
    
    a = a.map(e => e.split(',').map(e => Number(e)));
    console.log(a);

    const answer = [a[0][0]];
    for (let i = 1; i < a.length; i++) {
        a[i].sort();
        let j = 0;
        while (j < a[i - 1].length) {
            if (a[i - 1][j] !== a[i][j]) break;
            j++;
        }
        answer.push(a[i][j]);
    }

    return answer;
}

console.log(solution("{{2},{2,1},{2,1,2},{2,1,2,4}}"))