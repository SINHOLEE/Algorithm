// input 보일러 플레이트
process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/**
 * input 예시
 * 2
 * 4
 * 1 2 3 4
 * 3
 * 4 4 4
 */
function main() {
    let t = parseInt(readLine());
    while (t--) {
        const n = readLine();
        const arr = readLine().split(" ");
        console.log(n, arr)
    }
}




