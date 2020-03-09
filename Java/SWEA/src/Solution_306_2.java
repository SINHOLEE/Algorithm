import java.util.Scanner;

public class Solution_306_2 {
	static int T;
	public static void main(String[] args) throws Exception {
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner sc = new Scanner(System.in);
//		T = Integer.parseInt(br.readLine());
		T = sc.nextInt();
		for(int t = 1; t<= T; t++) {
//			StringTokenizer st = new StringTokenizer(br.readLine());
			
//			int n = Integer.parseInt(st.nextToken());
//			int m = Integer.parseInt(st.nextToken());
			int n = sc.nextInt();
			int m = sc.nextInt();
			String[][] dp = new String[n][m];	
			char[][] mat = new char[n][m];
			for (int i = 0; i < n; i++) {
				String words = sc.next().trim();
				for (int j = 0; j < m; j++) {
					mat[i][j] = words.charAt(j);
					
				}
//				mat[i] = br.readLine().trim().toCharArray();
				
			}
			dp[0][0] = Character.toString(mat[0][0]);
			for (int i = 0; i < n; i++) {
				// 가로 먼저 Xj X                        
				for (int j = 0; j < m-1; j++) {
					if (dp[i][j+1]==null) {
						dp[i][j+1] = dp[i][j] + Character.toString(mat[i][j+1]);
					}else {
						String temp1 = dp[i][j] + Character.toString(mat[i][j+1]);
						if(temp1.compareTo(dp[i][j+1]) < 0) {
							dp[i][j+1] = temp1;
						}
					}
				}
				// i가 마지막 직전까지는 밑으로 계산해주자.
				if(i <n-1) {
					for (int j = 0; j < m; j++) {
						if(dp[i+1][j]==null) {
							dp[i+1][j] = dp[i][j] + Character.toString(mat[i+1][j]);
						}else {
							String temp2 = dp[i][j] + Character.toString(mat[i+1][j]);
							if(temp2.compareTo(dp[i+1][j]) < 0) {
								dp[i+1][j] = temp2;
							}
						}						
					}					
				}
			}			
			System.out.println("#"+t+" "+dp[n-1][m-1]);
		}
		
	}

}
