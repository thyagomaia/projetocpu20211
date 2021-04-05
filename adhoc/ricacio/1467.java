import java.io.IOException;
 import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
    Scanner in = new Scanner(System.in);
 int a,b,c;
 String res = "";
 while(in.hasNext()){
  a = in.nextInt();
  b = in.nextInt();
  c = in.nextInt();
  if (a != b && a != c) {
                res = "A";
            } else if (b != a && b != c) {
                res = "B";
            }else if (c != a && c !=b) {
                res = "C";
            }else {
                res = "*";
            }
            System.out.println(res);
    }
    in.close();
 
    }
 
}