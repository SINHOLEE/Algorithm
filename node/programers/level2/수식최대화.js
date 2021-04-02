// 2:54
function operate(a, b, ep) {
	if (ep === "+") {
		return a + b;
	}
	if (ep === "*") {
		return a * b;
	}
	if (ep === "-") {
		return a - b;
	}
}

const withOperator = (opArg) => (expressionArr) => {
	if (expressionArr.length === 1) {
		return expressionArr[0];
	}
	for (let i = 0; i < expressionArr.length; i++) {
		if (expressionArr[i] === opArg) {
			let left = expressionArr[i - 1];
			let right = expressionArr[i + 1];
			const newExpressionArr = [
				...expressionArr.slice(0, i - 1),
				operate(left, right, opArg),
				...expressionArr.slice(i + 2),
			];
			return withOperator(opArg)(newExpressionArr);
		}
	}
	return expressionArr;
};

const add = withOperator("+");
const minus = withOperator("-");
const multiple = withOperator("*");

function solution(expression) {
	const expressionArr = expression
		.replace(/\-/g, " - ")
		.replace(/\*/g, " * ")
		.replace(/\+/g, " + ")
		.split(" ")
		.map((ep) => (/\d/.test(ep) ? parseInt(ep) : ep));

	const results = [
		add(multiple(minus(expressionArr))),
		add(minus(multiple(expressionArr))),
		multiple(add(minus(expressionArr))),
		multiple(minus(add(expressionArr))),
		minus(multiple(add(expressionArr))),
		minus(add(multiple(expressionArr))),
	].map(Math.abs);
	return Math.max(...results);
}

// function solution(expression) {
// 	function calc(a, b, op) {
// 		if (op === "*") {
// 			return a * b;
// 		}
// 		if (op === "m") {
// 			return a - b;
// 		}
// 		return a + b;
// 	}

// 	function genNewExp(exp, idx) {
// 		const op = exp[idx];
// 		let leftEnd = 0;
// 		let left = parseInt(exp.slice(0, idx));
// 		let rightStart = exp.length;
// 		let right = parseInt(exp.slice(idx + 1, exp.length));

// 		for (let i = idx - 1; i > 0; i--) {
// 			// 만약 끝까지 없다면 레프트는 첨부터 인덱스까지
// 			if (~["*", "m", "+"].indexOf(exp[i])) {
// 				left = parseInt(exp.slice(i + 1, idx));
// 				leftEnd = i + 1;
// 				break;
// 			}
// 		}

// 		for (let i = idx + 1; i < exp.length; i++) {
// 			if (~["*", "m", "+"].indexOf(exp[i])) {
// 				right = parseInt(exp.slice(idx + 1, i));
// 				rightStart = i;
// 				break;
// 			}
// 		}
// 		const prefix = exp.slice(0, leftEnd);
// 		const middle = calc(left, right, op).toString();
// 		const postfix = exp.slice(rightStart, exp.length);
// 		return prefix + middle + postfix;
// 	}
// 	function calcByOperatorPriority(exp, operatorPriority) {
// 		for (let i = 0; i < 3; i++) {
// 			if (~exp.indexOf(operatorPriority[i])) {
// 				const idx = exp.indexOf(operatorPriority[i]);
// 				const newExp = genNewExp(exp, idx);
// 				return calcByOperatorPriority(newExp, operatorPriority);
// 			}
// 		}
// 		return parseInt(exp);
// 	}
// 	expression = expression
// 		.split("")
// 		.map((e) => e.replace("-", "m"))
// 		.join("");

// 	const operatorPriorities = [
// 		["*", "m", "+"],
// 		["*", "+", "m"],
// 		["m", "*", "+"],
// 		["m", "+", "*"],
// 		["+", "m", "*"],
// 		["+", "*", "m"],
// 	];
// 	const results = operatorPriorities
// 		.map((operatorPriority) => calcByOperatorPriority(expression, operatorPriority))
// 		.map((result) => Math.abs(result));
// 	return Math.max(...results);
// }

let expression = "100-100-200*300-500+20";

console.log(solution(expression));
