import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	static String[] Player = {"A", "B", "C"};
	
	public static void resolver(byte[] Jogo) {
		
		List<String> Zero = new ArrayList<String>();
        List<String> Um = new ArrayList<String>();

        for(byte x = 0; x < 3; x++) {
        	if(Jogo[x] == 0) {
        		Zero.add(Player[x]);
        	}else {
        		Um.add(Player[x]);
        	}
        }

        
        if(Zero.size() == 0 || Um.size() == 0) {
        	System.out.println("*");
        }else {
        	if(Zero.size() == 1) {
        		System.out.println(Zero.get(0));
        	}else {
        		System.out.println(Um.get(0));
        	}
        }
	}
	
    public static void main(String[] args) {
    	Scanner scan = new Scanner(System.in);
    	
		List<byte[]> l = new ArrayList<byte[]>();

		try{
			while(true){
				byte[] x = {scan.nextByte(), scan.nextByte(), scan.nextByte()};
				l.add(x);
			}
		}catch(Exception e){
			
		}

		for(byte[] x : l){
			resolver(x);
		}
    }
}