/** 
 * 문제분석
 * 1. ?�� ?�� �? ?��
 *  M ?�� ?��간이 �??�� ?��?�� ?��?�� ?��?�� 미생물의 �? ?��
  
  * 주의?��?��.
  * ?��?��간이 �??���? 모든 군집?? 무조�? ?��?��?��.
  * ?��?��?�� 처리?�� ??�? �? 경우 ?��?���?
  *  1) ?���? ?��?��?�� 군집?�� ?��칸에 ?��착한 경우 - 말이 ?��?��
  *  2) ?��개의 군집?�� ?��칸에 ?��착한 경우 - 말이 ?��?��
  * 
  * ?��?��?�� 처리?���? ?��?? ??�? �? 경우
  *  1) ?���? ?��?��?�� 군집?�� ?��칸에 ?��착한 경우
  *  2) ?��개의 군집?�� ?��칸에 ?��착한 경우
  *   
  **/



public class Solution_2382 {
	static int di[] = {0, -1, 1, 0, 0};
	static int dj[] = {0, 0, 0, -1, 1};
	
	
	static int changeDir(int dir) {
		switch (dir) {
		case 1: return 2;
		case 2: return 1;
		case 3: return 4;
		case 4: return 3;
		}
		return -1;
	}
	static class Virus{
		int num; // ?��?��칸에 ?��?���? �? 번호�? 만들?�� ?���??��(?��?�� 매트�??��)
		int i, j;
		int cnt;
		int dir;
		
		public Virus(int num, int i, int j, int cnt, int dir) {
			this.num = num;
			this.i = i;
			this.j = j;
			this.cnt = cnt;
			this.dir = dir;
		}
		
	}
}


