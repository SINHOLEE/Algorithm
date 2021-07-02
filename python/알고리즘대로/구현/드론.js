// 1시간 20분 걸림
/**
 * 헤맨구간
 * 1. visited check를 하지 않아서 시간초과
 * 2. 축이 두개이기 때문에 실수할까봐 회전로직을 테스트 하면서 작성 -> 시간 오래걸림
 * 3. 3차원 배열 만드는데 어려움
 * 4. 회전 추상화 단계에서 a,b축까지 추상화할지, 좌우 회전까지만 할지 고민-> 시간 지체
 * 5. visited 입력할 때, a,b축 모두 다 입력하지 않아도 됨.
 *    왜냐? 드론a,b축은 항상 연결되어있으므로,
 *    a축과 a축의 방향만 알면 이전에 방문했는지 안했는지 파악할 수 있다.
 */

// 상 우 하 좌
const dy = [-1, 0, 1, 0];
const dx = [0, 1, 0, -1];

function solution(board) {
	const n = board.length;
	const m = board[0].length;
	const dron = {
		// d: a,b축이 바라보는 방향
		a: {y: 0, x: 0, d: 1},
		b: {y: 0, x: 1, d: 3},
		cnt: 0,
	};
	const visited = Array.from(Array(n), () => Array.from(Array(m), () => Array(4).fill(0)));
	visited[0][0][1] = 1;
	visited[0][1][3] = 1;
	const queue = [];
	queue.push(dron);
	while (queue) {
		const dron = queue.shift();
		const {a, b, cnt} = dron;
		if ((a.y === n - 1 && a.x === m - 1) || (b.y === n - 1 && b.x === m - 1)) {
			return cnt;
		}
		fourDirectionMove(dron, board, visited, queue, n, m);
		aTurn(dron, board, visited, queue, n, m);
		bTurn(dron, board, visited, queue, n, m);
	}
}

function fourDirectionMove(dron, board, visited, queue, n, m) {
	const {a, b, cnt} = dron;
	for (const kk of [0, 1, 2, 3]) {
		const ny = a.y + dy[kk];
		const nx = a.x + dx[kk];
		const nny = b.y + dy[kk];
		const nnx = b.x + dx[kk];
		// 벽 너머인지 체크 *2
		if (0 > ny || n <= ny || 0 > nx || m <= nx || 0 > nny || n <= nny || 0 > nnx || m <= nnx) {
			continue;
		}
		// 하나라도 기둥이 있는지 체크*2
		if (board[ny][nx] || board[nny][nnx]) {
			continue;
		}
		if (visited[ny][nx][a.d]) {
			continue;
		}
		visited[ny][nx][a.d] = 1;

		//문제 없으면 queue에 삽입
		queue.push({
			a: {y: ny, x: nx, d: a.d},
			b: {y: nny, x: nnx, d: b.d},
			cnt: cnt + 1,
		});
	}
}
function aTurn(dron, board, visited, queue, n, m) {
	const {y, x, d} = dron.a;
	const {cnt} = dron;
	for (const kk of [1, 3]) {
		const ny = y + dy[(d + kk) % 4];
		const nx = x + dx[(d + kk) % 4];
		const nny = y + dy[(d + kk) % 4] + dy[d];
		const nnx = x + dx[(d + kk) % 4] + dx[d];
		// 벽 너머인지 체크 *2
		if (0 > ny || n <= ny || 0 > nx || m <= nx || 0 > nny || n <= nny || 0 > nnx || m <= nnx) {
			continue;
		}
		// 하나라도 기둥이 있는지 체크*2
		if (board[ny][nx] || board[nny][nnx]) {
			continue;
		}
		// a축 기준, 바뀔 방향에 y,x축에서 visited체크
		// 바뀔 방향 === (d+kk)%4
		if (visited[y][x][(d + kk) % 4]) {
			continue;
		}
		//문제 없으면 queue에 삽입
		visited[y][x][(d + kk) % 4] = 1;

		queue.push({
			a: {y, x, d: (d + kk) % 4},
			b: {y: ny, x: nx, d: (d + kk + 2) % 4},
			cnt: cnt + 1,
		});
	}
}
function bTurn(dron, board, visited, queue, n, m) {
	const {y, x, d} = dron.b;
	const {cnt} = dron;
	for (const kk of [1, 3]) {
		const ny = y + dy[(d + kk) % 4];
		const nx = x + dx[(d + kk) % 4];
		const nny = y + dy[(d + kk) % 4] + dy[d];
		const nnx = x + dx[(d + kk) % 4] + dx[d];
		// 벽 너머인지 체크 *2
		if (0 > ny || n <= ny || 0 > nx || m <= nx || 0 > nny || n <= nny || 0 > nnx || m <= nnx) {
			continue;
		}
		// 하나라도 기둥이 있는지 체크*2
		if (board[ny][nx] || board[nny][nnx]) {
			continue;
		}
		// a축 기준, 바뀔 방향에 y,x축에서 visited체크
		// 바뀔 방향 === (d+kk)%4
		if (visited[y][x][(d + kk) % 4]) {
			continue;
		}
		//문제 없으면 queue에 삽입
		visited[y][x][(d + kk) % 4] = 1;

		queue.push({
			a: {y: ny, x: nx, d: (d + kk + 2) % 4},
			b: {y, x, d: (d + kk) % 4},
			cnt: cnt + 1,
		});
	}
}
console.log(
	solution([
		[0, 0, 0, 1, 1],
		[0, 0, 0, 1, 0],
		[0, 1, 0, 1, 1],
		[1, 1, 0, 0, 1],
		[0, 0, 0, 0, 0],
	]),
);
