import java.io.IOException;
import java.util.Scanner;

public class Main {	
    public static void main(String[] args) throws IOException {
    	Scanner scanner = new Scanner(System.in);
    	int n = scanner.nextInt();
    	int t, anos;
        while (scanner.hasNext()) {
            for (int i = 0; i < n; i++) {
                t = scanner.nextInt();
                if (t >= 2015) {
                    anos = t - 2014;
                    System.out.println(anos + " A.C.");
                } else {
                    anos = 2015 - t;
                    System.out.println(anos + " D.C.");
                }   
            }
    	}
        scanner.close();
    }
}