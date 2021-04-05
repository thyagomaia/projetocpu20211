import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner entrada = new Scanner(System.in);
        String a, b;
        int i, x1, x2;
        a = entrada.nextLine();
        b = entrada.nextLine();
        String[] itemsA = a.split(" ");
        String[] itemsB = b.split(" ");
        int P = Integer.parseInt(itemsA[0]);
        int N = Integer.parseInt(itemsA[1]);
        int[] alt = new int[N+1];
        for (i = 0; i < N; i++) {
          alt[i] = Integer.parseInt(itemsB[i]);
        }
        for (i = 0; i < N - 1; i++) {
          x1 = alt[i];
          x2 = alt[i+1];
          if ((x1 - x2) > P || (x2 - x1) > P) {
            System.out.println("GAME OVER");
            return;       
          }      
        }
        System.out.println("YOU WIN");
        entrada.close();
    }
}