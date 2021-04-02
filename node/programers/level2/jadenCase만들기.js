// 12:38
const changeToUpperOnlyFirst = (value) => {
	let res = "";
	for (let i = 0; i < value.length; i++) {
		let char = value[i].toLowerCase();
		if (i === 0) {
			char = value[i].toUpperCase();
		}
		res += char;
	}
	return res;
};

function solution(s) {
	return s.split(" ").map(changeToUpperOnlyFirst).join(" ");
}

console.log(solution("3people unFollowed me"));
console.log(solution("for the last week"));
