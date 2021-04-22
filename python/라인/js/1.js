/**
 * @param string
 * @returns boolean
 */
const isNumber = (string) => {
	return Array.from(string).every(
		(char) =>
			'0'.charCodeAt() <= char.charCodeAt() &&
			char.charCodeAt() <= '9'.charCodeAt()
	);
};

/**
 * @param string
 * @returns boolean
 */
const isLowerCharacter = (string) => {
	return Array.from(string).every(
		(char) =>
			'a'.charCodeAt() <= char.charCodeAt() &&
			char.charCodeAt() <= 'z'.charCodeAt()
	);
};
/**
 * @param string
 * @returns boolean
 */
const isUpperCharacter = (string) => {
	return Array.from(string).every(
		(char) =>
			'A'.charCodeAt() <= char.charCodeAt() &&
			char.charCodeAt() <= 'Z'.charCodeAt()
	);
};

/**
 * @param string
 * @returns boolean
 */
const isLetters = (string) => {
	return isLowerCharacter(string) || isUpperCharacter(string);
};

/**
 * commands를 받고 program과 flag_args로 나누는 함수
 * @param string
 * @returns [string, string]
 */
const split_progran_and_flag_arguments = (command) => {
	const copied_command = command;
	const first_white_space_idx = copied_command.indexOf(' ');
	return [
		copied_command.slice(0, first_white_space_idx),
		copied_command.slice(first_white_space_idx + 1),
	];
};

const isSameProgram = (a, b) => {
	return a === b;
};

const get_flag_dict = (flag_rules) => {
	const flag_dic = {};
	for (let flag_rule of flag_rules) {
		const [flag_name, rule] = flag_rule.split(' ');
		flag_dic[flag_name] = rule;
	}
	return flag_dic;
};

const checkCliConditions = (program, command, flag_dic) => {
	const [splited_program, flag_args] = split_progran_and_flag_arguments(
		command
	);
	if (!isSameProgram(program, splited_program)) {
		return false;
	}
	const flag_args_arr = flag_args.split(' ');
	for (let i = 0; i < flag_args_arr.length; i++) {}
	console.log(flag_dic);

	// 각 flag_argment에 타입과 일치한다.
};

function solution(program, flag_rules, commands) {
	var answer = [];
	const flag_dic = get_flag_dict(flag_rules);
	for (let command of commands) {
		answer.push(checkCliConditions(program, command, flag_dic));
	}

	return answer;
}
solution(
	'line',
	['-s STRING', '-n NUMBER', '-e NULL'],
	['line -n 100 -s hi -e', 'lien -s Bye']
);
