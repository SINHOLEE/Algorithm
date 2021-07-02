const isWall = (x, y, n, m) => {
	if (x < 0 || x > m - 1 || y < 0 || y > n - 1) return true;
	return false;
};
var shortestPath = function (grid, k) {
	const m = grid.length;
	const n = grid[0].length;
	const BFS = () => {
		const visited = Array.from(Array(m), () => Array(n).fill(0));
		const shieldDp = Array.from(Array(m), () => Array(n).fill(20000));
		const queue = [{x: 0, y: 0, shield: k, count: 0}];
		const direction = [
			[0, 1],
			[1, 0],
			[0, -1],
			[-1, 0],
		];
		visited[0][0] = 1;
		while (queue.length > 0) {
			const {x, y, shield, count} = queue.shift();

			console.log(x, y);
			console.log(visited);
			console.log(shieldDp);
			console.log();
			console.log();
			console.log();
			if (x === m - 1 && y === n - 1) {
				console.log(x, y);
				console.log(visited);
				return count;
			}

			for (const [dx, dy] of direction) {
				const xx = x + dx;
				const yy = y + dy;
				if (isWall(xx, yy, n, m)) continue;
				if (visited[xx][yy] && grid[xx][yy] && shield === 0) continue;
				const prevSheild = shieldDp[xx][yy];
				if (grid[xx][yy] && prevSheild <= 0) continue;
				if (visited[xx][yy] && grid[xx][yy] && prevSheild <= shield) continue;
				queue.push({
					x: xx,
					y: yy,
					shield: grid[xx][yy] ? shield - 1 : shield,
					count: count + 1,
				});
				visited[xx][yy] = count + 1;
				shieldDp[xx][yy] = grid[xx][yy] ? shield - 1 : shield;
			}
		}
		return -1;
	};
	return BFS();
};

console.log(
	shortestPath(
		[
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
			[0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
			[0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
			[0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		],
		1,
	),
);
[
	[1, 1, 1, 1, 1, -2, 1, 1, 1, 1],
	[1, -6, -4, -4, -2, -2, -2, 0, 0, 20000],
	[1, -5, -4, -1, -3, -2, -1, -1, 20000, 20000],
	[1, -6, 0, -5, -4, -5, -1, 20000, 20000, 20000],
	[1, -5, -3, 0, -3, 0, 20000, 20000, 20000, 20000],
	[1, -6, -5, -6, -2, 20000, 20000, 20000, 20000, 20000],
	[1, -5, -5, -1, 20000, 20000, 20000, 20000, 20000, 20000],
	[1, -6, -1, 20000, 20000, 20000, 20000, 20000, 20000, 20000],
	[1, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000],
	[20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000],
	[20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000],
	[20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000],
];
