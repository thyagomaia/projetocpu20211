import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {; 

	public static String resolver(List<String> l){
		int ls = l.size();

		for (int i = 0; i < ls - 1; i++) {
			if(!l.get(i).equals(l.get(i+1))){
				return "ingles";
			}
		}

		return l.get(0);
	}

    public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		List<String> l;
		int x;

		int N = scan.nextInt();
	
		for(int n = 0; n < N; n++){
			l = new ArrayList<String>();
			x = scan.nextInt();

			for (int i = 0; i < x; i++) {
				l.add(scan.next());
			}

			System.out.println(resolver(l));
		}

    }
}