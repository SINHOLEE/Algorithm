import java.util.LinkedList;
import java.util.Queue;

public class BFS2 {
	static int[][] map;
	static boolean[][] visited;
	static int[] dy = {0, 0, 1, -1};
	static int[] dx = {1, -1, 0, 0};
	static int N, ans;
	public static void main(String[] args) {
		
	}
	static void bfs() {
		Queue<Point> q = new LinkedList<>();
		q.add(new Point(0, 0));
		boolean [][] visited = new boolean[N][N];
		visited[0][0] = true;
		
		while(!q.isEmpty()) {
			int size = q.size();
			
			for (int s= 0; s<size;s++) {
				Point now = q.poll();
				
				
			}
		}
	}
	
	static class Point{
		int i, j;
		public Point(int i, int j) {
			this.i = i;
			this.j = j;	
		}
	}

}
