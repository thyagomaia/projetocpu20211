import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a,b,c;
        String res = "";
        while (scanner.hasNext()) {
            a = scanner.nextInt();
            b = scanner.nextInt();
            c = scanner.nextInt();
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
        scanner.close();
    }
}