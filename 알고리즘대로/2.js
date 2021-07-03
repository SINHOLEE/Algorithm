const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();
const small_vowel = ['a', 'i', 'y', 'e', 'o', 'u'];
const small_consonant = [
	'b',
	'k',
	'x',
	'z',
	'n',
	'h',
	'd',
	'c',
	'w',
	'g',
	'p',
	'v',
	'j',
	'q',
	't',
	's',
	'r',
	'l',
	'm',
	'f',
];
const big_vowel = ['A', 'I', 'Y', 'E', 'O', 'U'];
const big_consonant = [
	'B',
	'K',
	'X',
	'Z',
	'N',
	'H',
	'D',
	'C',
	'W',
	'G',
	'P',
	'V',
	'J',
	'Q',
	'T',
	'S',
	'R',
	'L',
	'M',
	'F',
];
const vowel_num = 6;
const consonant_num = 20;
while (1) {
	const str = input();
	if (str === '' || str == undefined || str == null) break;
	let ans = '';
	for (const char of str) {
		const char_num = char.charCodeAt();
		if (65 <= char_num && char_num <= 90) {
			if (big_vowel.indexOf(char) !== -1) {
				ans += big_vowel[(big_vowel.indexOf(char) + 9) % vowel_num];
			} else {
				ans +=
					big_consonant[(big_consonant.indexOf(char) + 30) % consonant_num];
			}
		} else if (97 <= char_num && char_num <= 122) {
			if (small_vowel.indexOf(char) !== -1) {
				ans += small_vowel[(small_vowel.indexOf(char) + 9) % vowel_num];
			} else {
				ans +=
					small_consonant[(small_consonant.indexOf(char) + 30) % consonant_num];
			}
		} else ans += char;
	}
	console.log(ans);
}
