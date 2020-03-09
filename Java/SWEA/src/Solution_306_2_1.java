import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.PriorityQueue;

public class Solution_306_2_1 {
	static int T;
	static int[] dy = {0, 1};
	static int[] dx = {1, 0};
	static boolean [][] visited;
	static String ans;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		//		Scanner sc = new Scanner(System.in);
		//		T = sc.nextInt();
		int T = Integer.parseInt(br.readLine());

		for(int t = 1; t<= T; t++) {
			ans = "";
			String [] line = br.readLine().split(" ");
			int n = Integer.parseInt(line[0]);
			int m = Integer.parseInt(line[1]);

			//			int n = sc.nextInt();
			//			int m = sc.nextInt();	
			char[][] mat = new char[n][m];
			visited = new boolean[n][m];

			for (int i = 0; i < n; i++) {
				mat[i] = br.readLine().toCharArray();
			}
			visited[0][0] = true;
			PriorityQueue<Point> queue = new PriorityQueue<>();
			queue.add(new Point(0, 0, mat[0][0]));
			ArrayList list = new ArrayList<>();
			bw.write("#"+t+" ");

			while (!queue.isEmpty()) {
				int size = queue.size();

				Point first = queue.peek(); // 현재 큐에 있는 글자수 중 알파벳 숫자중 제일 빠른걸 확보
				for(int s=0; s<size;s++) {
					Point now = queue.poll();
					if(first.ch == now.ch) {
						for(int d=0; d<2; d++) {
							int ni = now.i+dy[d];
							int nj = now.j+dx[d];

							if (ni>=0 && ni<n && nj>=0 && nj<m && !visited[ni][nj]) {
								list.add(new Point(ni, nj, mat[ni][nj]));
								visited[ni][nj] = true;
							}	
						}
					} else {
						break;
					}

				}
				queue.clear();
				queue.addAll(list);
				list.clear();
				bw.write(first.ch);
			}
			bw.write("\n");	
		}
		br.close();
		bw.flush();
		bw.close();
	}
	static class Point implements Comparable<Point>{
		int i,j;
		char ch;
		public Point(int i, int j, char ch) {
			this.i = i;
			this.j = j;
			this.ch = ch;
		}
		public int compareTo(Point o) {
			return this.ch-o.ch;
		}
	}
}
