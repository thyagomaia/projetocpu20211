import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		boolean up;

		String[] x2;
		
		try{
			while(true){
				up = true;
				x2 = scan.nextLine().split("");
	 
				for (String string : x2) {
					char z = string.toUpperCase().charAt(0);
					if(z >= 'A' && z <= 'Z'){
					//if(!string.equals(" ")){
						if(up){
							System.out.print(string.toUpperCase());
							up = false;
						}else{
							System.out.print(string.toLowerCase());
							up = true;
						}
					}else{
						System.out.print(string);
					}
				}
				System.out.println("");
			}
		}catch(Exception e){

		}
	}
}