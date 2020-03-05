import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution_306_1 {
	static int T;
	static int arr[];
	static int left;
	static int right;
	static int total;
	static int k ;  // 필요 없을것 같다.
	static int idx;
	/**
	 * @param args
	 * @throws NumberFormatException
	 * @throws IOException
	 */
	public static void main(String[] args) throws NumberFormatException, IOException {
		Scanner sc = new Scanner(System.in);

		T = sc.nextInt();
		for(int t=1; t<=T; t++) {
		
			int n = sc.nextInt();
			arr = new int[n+1];
			
			for (int i = 0; i < n; i++) {
				arr[i] = sc.nextInt();
				
			}
			arr[n] = -1;
			left = 0;
			right = 0;
			total = 0;
			k  = -1;  // 필요 없을것 같다.
			idx = 0;
			while (idx <n) {
				while (idx <n&& arr[idx] <arr[idx+1] ) {
					left += 1;
					idx+=1;
				}
				k = idx;
				while (idx <n&&arr[idx] > arr[idx+1] ) {
					right += 1;
					idx+=1;
				}
				if (idx == n&&right !=0) {
					right -= 1;
				}
				total += left * right;
				left = 0;
				right=0;
			}
			System.out.println("#"+t+" "+total);
		}
	}
}
