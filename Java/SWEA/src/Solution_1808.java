import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class Solution_1808 {
    static int[] arr;
    static int target;
    static int min_cnt;
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for ( int t = 1; t<=T; t++) {
        	min_cnt = Integer.MAX_VALUE;
        	arr = new int[10];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0;i<10; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
            target = Integer.parseInt(br.readLine());
            dfs(0, 0);
             
            if (min_cnt == Integer.MAX_VALUE) {
                System.out.println("#"+t+" "+ "-1");
            }else {
                min_cnt+=1;
                System.out.println("#"+t+" "+ min_cnt);
            }   
        }
    }
    private static void dfs(int num, int cnt) {
        if (cnt > min_cnt) {
            return;
        }
        if (num > target) {
            return;
        }
        if (num == target) {
            min_cnt = Math.min(cnt, min_cnt);
            return;
        }
        for (int j = 0; j<10; j++) {
            if (arr[j] == 0) {
                continue;
            }
            if(j == 0) {
                continue;
            }
            dfs(num * 10 + j, cnt + 1);
            if (j == 1) {
                continue;
            }
            if (num ==0) {
                continue;
            }
            dfs(num * j, cnt+2);
        }
             
    }
 
}