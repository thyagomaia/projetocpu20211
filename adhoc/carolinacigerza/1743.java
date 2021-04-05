import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner entrada = new Scanner(System.in);
        String a, b;
        int i;
        a = entrada.nextLine();
        b = entrada.nextLine();
        String[] itemsA = a.split(" ");
        String[] itemsB = b.split(" ");    
        for (i = 0; i < 5; i++) {
          if (Integer.parseInt(itemsA[i]) + Integer.parseInt(itemsB[i]) != 1) {
            System.out.println("N");
            return;
          }
        }
        System.out.println("Y");
        entrada.close();   
    }
}