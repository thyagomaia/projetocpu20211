import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner entrada = new Scanner(System.in);
        String x, r = "k";
        int A, B, C;
        do {
          x = entrada.nextLine();
          String[] itemsX = x.split(" ");
          A = Integer.parseInt(itemsX[0]);
          B = Integer.parseInt(itemsX[1]);
          C = Integer.parseInt(itemsX[2]);
          if (A == B && A == C) {
            r = "*";
          } else if (A == B && A != C) {
            r = "C";
          } else if (A != B && B == C) {
            r = "A";
          } else if (A != B && A == C) {
            r = "B";
          }
          System.out.println(r);
        } while (entrada.hasNext());
        entrada.close();
        return;
    }
}