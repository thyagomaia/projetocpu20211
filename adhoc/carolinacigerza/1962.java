import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
         Scanner teclado = new Scanner(System.in);
         int n, t, i, ano;    
         n = teclado.nextInt();
         String anos[] = new String[n];    
         for (i = 0; i < n; i++) {
              t = teclado.nextInt();
              if (t > 2015) {
                ano = t - 2014;
                anos[i] = ano + " A.C.";
              } 
              else if (t < 2015) {
                ano = 2015 - t;
                anos[i] = ano + " D.C.";
              }
              else {
                anos[i] = "1 A.C.";
              }      
         }
         for (i = 0; i < n; i++) {
             System.out.println(anos[i]);
         }
    }
}