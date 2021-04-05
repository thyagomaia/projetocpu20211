import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		String[] s;
		String[] s2;
		int Num;

		int n = scan.nextInt();

		for (int i = 0; i < n; i++) {
			s = scan.next().split("");
			s2 = scan.next().split("");

			Num = s.length;

			if(s2.length > s.length){
				Num = s2.length;
			}

			for (int j = 0; j < Num; j++) {	
				try{
					System.out.print(s[j]);
				}catch(Exception e){}
				
				try{
					System.out.print(s2[j]);
				}catch(Exception e){}
			}

			System.out.println("");
		}
	}
}