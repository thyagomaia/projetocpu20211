import java.util.Scanner;

public class Main {

	public static void resolver(){
				
	}

    public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		byte AP = scan.nextByte();
		byte NC = scan.nextByte();

		byte[] AC = new byte[NC];

		String str = "YOU WIN";

		for(byte x = 0; x < NC; x++){
			AC[x] = scan.nextByte();
		}

		for(byte x = 0; x < NC - 1; x++){
			int dif = AC[x+1] - AC[x];
			
			if(!(dif <= AP && dif >= -AP)){
				str = "GAME OVER";
				break;
			}
		}

		System.out.println(str);
	}
}