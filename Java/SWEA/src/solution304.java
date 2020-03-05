
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class solution304 {
	static int result;
	static int n, m;
	static int [][] mat;
	static int [][][][] dp;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		
		int T =Integer.parseInt(br.readLine());
		for(int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken()); 
			m = Integer.parseInt(st.nextToken());
			mat = new int[n][m];
			dp = new int[n][m][n+1][m+1];
			
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0;j < m; j++ ) {
					mat[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
//								sy, sx, ey, ex
			result = solution(0, 0, n, m);
			System.out.println("#" + tc + " "+ result);
		}
	}
	private static int solution(int sy, int sx, int ey, int ex) {
		if(ey-sy <= 1 && ex-sx <= 1){
			return 0;
		}
		if (dp[sy][sx][ey][ex] == 0) {
			dp[sy][sx][ey][ex] =Integer.MAX_VALUE;
		}else {
			return dp[sy][sx][ey][ex];
		}
		
		int my_sum1 = 0;

		for (int i = sy; i<ey; i++) {
			for (int j = sx; j<ex; j++) {
				my_sum1 += mat[i][j];
				}
			} 
	
		for (int i = sy+1; i<ey; i++) {
				int temp1 = solution(sy, sx, i, ex) + solution(i, sx, ey, ex) + my_sum1;
				dp[sy][sx][ey][ex] = Math.min(temp1, dp[sy][sx][ey][ex]);
		}
		
		for (int j = sx+1; j<ex; j++) {
				int temp2 = solution(sy, sx, ey, j ) + solution(sy, j, ey, ex)+my_sum1;
				dp[sy][sx][ey][ex] = Math.min(temp2, dp[sy][sx][ey][ex]);

		}
		return dp[sy][sx][ey][ex];
	}
}
