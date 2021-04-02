//12:55
const fileNameParser = (file, index) => {
	let isNumStarted = false;
	let isTailStarted = false;
	let head = "";
	let num = "";
	let tail = "";
	for (let i = 0; i < file.length; i++) {
		const currentChar = file[i];
		if (!isNumStarted && /\d/.test(currentChar)) {
			isNumStarted = true;
		}
		if (isNumStarted && i !== 0 && !/\d/.test(file[i])) {
			isTailStarted = true;
		}

		if (!isNumStarted && !isTailStarted) {
			head += currentChar;
		}
		if (isNumStarted && !isTailStarted) {
			num += currentChar;
		}
		if (isNumStarted && isTailStarted) {
			tail += currentChar;
		}
	}
	return {
		head: head.toLocaleLowerCase(),
		num: parseInt(num),
		tail,
		index,
		originFile: file,
	};
};

const comparable = (a, b) => {
	if (a.head !== b.head) {
		return a.head < b.head ? -1 : 1;
	}
	if (a.num !== b.num) {
		return a.num - b.num;
	}
	return a.index - b.index;
};

//12:50
function solution(files) {
	return files
		.map(fileNameParser)
		.sort(comparable)
		.map((file) => file.originFile);
}

const isEqual = (a, b) => {
	return JSON.stringify(a) === JSON.stringify(b);
};
console.log(
	isEqual(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]), [
		"img1.png",
		"IMG01.GIF",
		"img02.png",
		"img2.JPG",
		"img10.png",
		"img12.png",
	]),
);
console.log(
	isEqual(
		solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]),
		["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"],
	),
);
