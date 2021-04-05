import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {

	public static void resolver(){
				
	}

    public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int Td = -1;
		
		
		String format = "0.00";
		DecimalFormatSymbols symb = new DecimalFormatSymbols(new Locale("en"+"USA"));
		DecimalFormat df = new DecimalFormat(format, symb);

		List<String> resp;

		while(true){
			resp = new ArrayList<String>();
			Td = scan.nextInt();
			
			if(Td == 0) {
				break;
			}
			
			for(int x = 0; x < Td; x++){
				int qt = scan.nextInt();
				double alt = Double.parseDouble(scan.next());
				double base = Double.parseDouble(scan.next());
				
				Double r = (((base + alt) * 5) / 2) * qt;

				String str = "Size #"+(x+1)+":\n"+
						  "Ice Cream Used: "+df.format(r)+" cm2";
				System.out.println(str);
				//resp.add(str);
			}
			
//			for(String x : resp){
//				System.out.println(x);
//			}
			System.out.println("");
		}
	}
}