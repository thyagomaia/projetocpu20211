import java.util.Scanner;

public class Main {

	public static void res(String n){
		boolean fim = false;
		for (String x : n.split("")) {
			if(!(x.equals("0") && !fim)){
				System.out.print(x);
				fim = true;
			}
		}
		System.out.println("");
	}
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		byte d;
		String n;

		while(true){
			d = scan.nextByte();
			n = scan.next();
			
			if(d == 0 && n.equals("0")){
				break;
			}
				
			n = n.replace(""+d, "");
				
			if(n.equals("") || n.replace("0", "").equals("")) {
				System.out.println("0");
			}else{
				res(n);
			}
		}
	}
}