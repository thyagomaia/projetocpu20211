import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = 0;
        int [] conec1 = new int [5];
        int [] conec2 = new int [5];
        int res = 0;
        String rs;
        while (scanner.hasNext()) {
            for (int j = 0; j < 5; j++) {
                conec1[j] = scanner.nextInt();
            }
            for (int x = 0; x < 5; x++) {
                conec2[x] = scanner.nextInt();
            }
            for (int c = 0; c < 5; c++) {
                if (conec1[n] + conec2[n] == 1) {
                    n++;
                    res++;
                }
            }
            if (res == 5) {
                rs = "Y";
            } else {
                rs = "N";
            }
            n = 0;
            res = 0;
            System.out.println(rs);
        }
        scanner.close();
    }
}