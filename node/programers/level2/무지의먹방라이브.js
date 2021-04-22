// 8:50

function solution(food_times, k) {
	let roundAndIndexArr = food_times.map((food_time, index) => ({
		food_time,
		index: index + 1,
	}));

	if (k >= roundAndIndexArr.reduce((prev, item) => prev + item.food_time, 0)) {
		return -1;
	}
	const dict = food_times.reduce((prev, curr, index) => {
		prev[curr] = prev[curr] ? prev[curr] + 1 : 1;
		return prev;
	}, {});
	let base = 0;
	let len = roundAndIndexArr.length;
	const sortedDict = Object.keys(dict)
		.map((key) => ({ food_time: parseInt(key), round: dict[key] }))
		.sort((a, b) => b.food_time - a.food_time);
	while (sortedDict.length) {
		const { food_time, round } = sortedDict.pop();
		if (len * (food_time - base) >= k) {
			break;
		}
		k -= len * (food_time - base);
		base = food_time;
		len -= round;
	}
	roundAndIndexArr = roundAndIndexArr.filter((item) => item.food_time > base);
	return roundAndIndexArr[parseInt(k % len)].index;
}

console.log(solution([1], 1));
console.log(solution([3, 1, 2], 5));
console.log(solution([9, 6, 4, 5, 6], 1000000));
console.log(solution([4, 2, 3, 6, 7, 1, 5, 8], 16));
