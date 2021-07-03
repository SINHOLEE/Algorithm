let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

function isRightPatern(signal) {
	// 시작과 끝을 명시적으로 선언해야한다.
	const reg = /^((100)(0*)(1+)|01)+$/;
	const res = reg.test(signal);
	return res ? 'YES' : 'NO';
}

const n = parseInt(input.shift());
const inputs = input;

for (let i = 0; i < n; i++) {
	console.log(isRightPatern(inputs[i]));
}

// 참고 : https://wodyios.tistory.com/22
