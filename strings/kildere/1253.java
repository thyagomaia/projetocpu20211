import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int n = scan.nextInt();
		String s;
		int n2;

		for (int i = 0; i < n; i++) {
			s = scan.next();
			n2 = scan.nextInt();

			for(char c : s.toCharArray()){
				int p = c - n2;
				
				if(p < 'A'){
					System.out.print((char) (p + 26));
				}else{
					System.out.print((char) p);
				}
			}

			System.out.println("");
		}
	}
}