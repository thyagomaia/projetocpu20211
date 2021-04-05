import java.util.Scanner;

public class Main {

	public static void resolver(){
				
	}

    public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int Casos = scan.nextInt();

		String str;
		
		int ano;
		
		for(int x = 0; x < Casos; x++){
			str = " D.C.";
			ano = 2015 - scan.nextInt();
			
			if(ano <= 0) {
				ano--;
				ano = ano * -1;
				str = " A.C.";
			}
			
			System.out.println(ano + str);
		}
	}
}