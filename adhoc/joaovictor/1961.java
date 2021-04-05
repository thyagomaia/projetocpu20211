import java.util.Scanner;

public class Main {
    public static void main(String[] args){
    	Scanner leitor = new Scanner(System.in);
        int p = 0;
        int n = 0;
    	boolean win = true;
    	while (leitor.hasNext()) {
        win = true;
    	p = leitor.nextInt();
    	n = leitor.nextInt();
        int pulos[] = new int[n];
            for (int i = 0; i < n; i++) {
                pulos[i] = leitor.nextInt();
            }
            for (int i = 0; i < (n-1); i++) {
                if ((pulos[i] - pulos[i+1]) < (-p)) win = false;
                else if ((pulos[i] - pulos[i+1]) > p) win = false; 
            }
            if (win) System.out.println("YOU WIN");
            else System.out.println("GAME OVER");
        }
        leitor.close();
    }
}