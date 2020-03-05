
import java.util.Scanner;

public class Solution_5684 {
	static int [][] graph;
	static int ans;
	static boolean [] visited;
	static int n, m;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int TC = sc.nextInt();
		for (int t = 1; t <= TC; t++) {
			ans = Integer.MAX_VALUE ;
			n = sc.nextInt();
			m = sc.nextInt();
			graph = new int [n+1][m+1];
			for (int j = 0; j < m; j++) {
				int s = sc.nextInt();
				int e = sc.nextInt();
				int c = sc.nextInt();
				
				graph[s][e] = c;	
			}
			for (int node = 1; node<=n; node++) {
				visited = new boolean[n+1];
				dfs(node, node, 0);
			}
			System.out.println("#"+t+" "+(ans==Integer.MAX_VALUE?-1:ans));
		}
	}
	static void dfs(int node, int start, int dist) {
		if ( node == start && visited[node]) {
			ans = Math.min(ans, dist);
			return;
		}
		if (ans <= dist) {
			return;
		}
		if(visited[node]) {
			return;
		}
		visited[node] = true;
		for (int i = 1; i<= n; i++) {
			if (graph[node][i] >0) {
				dfs(i, start, dist + graph[node][i]);
			}
		}
	}
}
