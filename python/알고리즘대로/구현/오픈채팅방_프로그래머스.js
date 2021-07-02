//11:30
//1차 11:52
// 2차 리펙터링 12:05
function solution(record) {
	const users = new Map();
	const logs = [];
	preProcess(users, logs, record);
	return answer(users, logs);
}

function preProcess(users, logs, record) {
	// enter or leave
	function addLog(userId, command) {
		logs.push({userId, command});
	}
	for (const re of record) {
		const parsedData = re.split(/ /);
		if (parsedData[0] === "Enter" || parsedData[0] === "Change") {
			// 'Enter', 'uid1234', 'Muzi'
			users.set(parsedData[1], parsedData[2]);
		}
		if (parsedData[0] === "Enter" || parsedData[0] === "Leave") {
			// [ 'Leave', 'uid1234' ]
			addLog(parsedData[1], parsedData[0]);
		}
	}
}

function answer(users, logs) {
	function getNameByUserId(id) {
		return users.get(id);
	}
	var result = [];
	for (const log of logs) {
		const temp =
			log.command === "Enter"
				? `${getNameByUserId(log.userId)}님이 들어왔습니다.`
				: `${getNameByUserId(log.userId)}님이 나갔습니다.`;
		result.push(temp);
	}
	return result;
}

console.log(
	solution([
		"Enter uid1234 Muzi",
		"Enter uid4567 Prodo",
		"Leave uid1234",
		"Enter uid1234 Prodo",
		"Change uid4567 Ryan",
	]),
);
