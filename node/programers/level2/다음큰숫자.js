// 8:27
function solution(n) {
	const originalBin = n.toString(2);
	const cntOne = originalBin.split("").filter((char) => char === "1").length;

	while (1) {
		n++;
		if (
			n
				.toString(2)
				.split("")
				.filter((char) => char === "1").length === cntOne
		) {
			break;
		}
	}
	return n;
}

for (let i = 1; i < 1000001; i++) {
	let start = Date.now();
	solution(i);
	let end = Date.now();
	if (end - start > 1) {
		console.log("time", i, end - start);
	}
}
// console.log(solution(78));
// console.log(solution(15));
