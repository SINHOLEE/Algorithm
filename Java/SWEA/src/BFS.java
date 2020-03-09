import java.util.LinkedList;
import java.util.Queue;

public class BFS {
	static int[][] map;
	static boolean[][] visited;
	static int[] dy = {0, 0, 1, -1};
	static int[] dx = {1, -1, 0, 0};
	static int N, ans;
	static class Point{
		int i, j, dist;
		public Point(int i, int j, int dist ) {
			this.i = i;
			this.j = j;
			this.dist = dist;			
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Queue<Point> q = new LinkedList<>();
		visited = new boolean [N][N];
		visited[0][0] = true;
		
		while(!q.isEmpty()) {
			Point now = q.poll();
			if (now.j == N-1 && now.i == N-1) {
				ans = now.dist;
				return;
			}
			
			for (int d=0; d<4; d++) {
				int ni = now.i+dy[d];
				int nj = now.j+dx[d];
				if(ni>=0 && ni <N && nj>= 0 && nj <N && map[ni][nj]==0 && !visited[ni][nj]) {
					q.add(new Point(ni, nj, now.dist+1));
					visited[ni][nj] = true;
				}
				
				
			}
		}
	}

}
