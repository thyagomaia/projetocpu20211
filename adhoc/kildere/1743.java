import java.util.Scanner;

public class Main {

	public static void resolver(){
				
	}

    public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		byte[] connect1 = new byte[5]; 
		char comp = 'Y';
		
		for(byte x = 0; x < 5; x++){
			connect1[x] = scan.nextByte();
		}

		for(byte x = 0; x < 5; x++){
			if(connect1[x] == scan.nextByte()){
				comp = 'N';
				break;
			}
		}

		System.out.println(comp);
	}
}