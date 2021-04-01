// 1:53
function solution(name) {
	const nameArr = name.split("");
	const startName = Array(name.length).fill("A");
	const queue = [];

	let min = 999999999999;
	queue.push([0, startName, 0]);
	while (queue.length) {
		const [cnt, res, cursor] = queue.shift();
		const resStr = res.join("");
		if (resStr === name) {
			min = Math.min(min, cnt);
			continue;
		}
		if (nameArr[cursor] === res[cursor]) {
			let rightPos = cursor;
			let rightCnt = 0;
			while (nameArr[rightPos] === res[rightPos]) {
				rightPos = parseInt((rightPos + 1) % nameArr.length);
				rightCnt++;
			}

			let leftPos = cursor;
			let leftCnt = 0;
			while (nameArr[leftPos] == res[leftPos]) {
				leftPos = parseInt((leftPos - 1 + nameArr.length) % nameArr.length);
				leftCnt++;
			}
			queue.push([cnt + rightCnt, res, rightPos]);
			queue.push([cnt + leftCnt, res, leftPos]);
		} else {
			const target = nameArr[cursor].charCodeAt();
			const minAdded = Math.min(target - 65, 91 - target);
			const newRes = [...res];
			newRes[cursor] = nameArr[cursor];
			const newResStr = newRes.join("");
			queue.push([cnt + minAdded, newRes, cursor]);
		}
	}
	return min;
}

console.log(solution("JAZ"));
console.log(solution("ABAAAABAB"));
console.log(solution("ABAAAABABAWWQWEQWEQWE"));
