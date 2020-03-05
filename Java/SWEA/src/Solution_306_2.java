import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution_306_2 {
	static String[][] dp;
	static char[][] mat;
	static int n, m, T;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());		
		for(int t = 1; t<= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			mat = new char[n][m];
			for (int i = 0; i < n; i++) {
				
				mat[i] = br.readLine().trim().toCharArray();
				
			}
			for (int i = 0; i < n; i++) {
				System.out.println(Arrays.toString(mat[i]));
			}
			
		}
		
	}

}
