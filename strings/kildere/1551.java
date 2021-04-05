import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int n = Integer.parseInt(scan.nextLine());
		String s;
		int tem;
		
		for (int i = 0; i < n; i++) {
			tem = 0;
			s = scan.nextLine();
			
			for (char j = 'a'; j <= 'z'; j++) {
				if(s.split((""+j)).length > 1){//tiver
					tem++;
				}
			}
			
			//System.out.println(tem);
			
			if(tem == 26){
				System.out.println("frase completa");
			}else if(tem >= 13){
				System.out.println("frase quase completa");
			}else{
				System.out.println("frase mal elaborada");
			}
		}
	}
}