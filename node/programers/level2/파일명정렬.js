//12:55
const fileNameParser = (file, index) => {
	let isNumStarted = false;
	let isTailStarted = false;
	let head = "";
	let num = "";
	let tail = "";
	for (let i = 0; i < file.length; i++) {
		const currentChar = file[i];
		if (isNumStarted && i !== 0 && !"0123456789".includes(file[i])) {
			isTailStarted = true;
		} else if (!isNumStarted && "0123456789".includes(currentChar)) {
			isNumStarted = true;
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

console.log(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]));
console.log(
	solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]),
);
