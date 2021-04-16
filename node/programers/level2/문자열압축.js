function solution(s) {
	let answer = 99999999;
	for (let k = 1; k < s.length + 1; k++) {
		// i == 문자열 압축할 갯수
		if (k === 3) {
			console.log("asd");
		}
		let temp = 0;
		let sss = "";
		let s_cnt = 0;
		let j = 0;
		for (j = 0; j < s.length; j += k) {
			if (sss === s.slice(j, j + k)) {
				s_cnt++;
			} else {
				sss = s.slice(j, j + k);
				if (s_cnt === 1) {
					temp += k;
					s_cnt = 0;
				} else if (s_cnt > 1) {
					temp += k + s_cnt.toString().length;
				}
				s_cnt = 1;
			}
		}
		if (s_cnt === 1) {
			temp += sss.length;
		} else if (s_cnt > 1) {
			temp += k + s_cnt.toString().length;
		}
		answer = Math.min(answer, temp);
	}

	return answer;
}

console.log(solution("abcabcdede"), 8);
