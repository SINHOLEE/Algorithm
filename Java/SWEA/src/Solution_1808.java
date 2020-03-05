
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Solution_1808 {
	static boolean[] arr;
	static int target;
	static int min_cnt;
	static int T;
	static int t;
	static int [] dp;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		arr = new boolean[10];
		for ( t = 1; t<=T; t++) {
			min_cnt = Integer.MAX_VALUE;
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0;i<10; i++) {
				if (Integer.parseInt(st.nextToken()) == 1) {
					arr[i] = true;
				}
			}
			target = Integer.parseInt(br.readLine());
			dp = new int[target+1];
			Arrays.fill(dp, Integer.MAX_VALUE);
			for (int i = 0;i<Math.min(10, target+1); i++) {				
				if (arr[i]) {					
					dp[i] = 1;
				}
			}
			for (int i = 0; i<=target;i++) {
				if (dp[i] == Integer.MAX_VALUE) {
					continue;
				}
				for (int j = 0; j<10; j++) {
					if(arr[j]) {
						continue;
					}
					int temp1 = i * j;
					if (target >= temp1) {
						dp[temp1] = Math.min(dp[temp1], dp[i] + 2);						
					}
				
					int temp2 = i * 10 + j;
					if (target >= temp2) {
						dp[temp2] = Math.min(dp[temp2], dp[i] + 1);						
					}
				}
			}
			System.out.println(dp[9]);
			System.out.println(dp[99]);
			if (dp[target] == Integer.MAX_VALUE) {
				System.out.println("#"+t+" "+ "-1");
			}else {
				dp[target] += 1;
				System.out.println("#"+t+" "+ dp[target]);
			}	
		}
	}

}
