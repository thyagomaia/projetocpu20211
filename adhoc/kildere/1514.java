import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	static List<Integer> result = new ArrayList<Integer>(); 

	public static void resolver(List<List<Integer>> lista){
		int cond1 = 1;
		int cond2 = 1;
		int cond3 = 1;
		int cond4 = 1;

		//por pessoa
		for(List<Integer> l : lista){
			boolean zero = false;
			boolean um = false;

			for(int x : l){
				if(x == 0){
					zero = true;
				}else{
					um = true;
				}
			}

			if(!zero){
				cond1 = 0;
			}
			if(!um){
				cond4 = 0;
			}
		}

		//por problema
		for(int Q = 0; Q < lista.get(0).size(); Q++){
			boolean zero = false;
			boolean um = false;
			
			for(byte P = 0; P < lista.size(); P++){
				if(lista.get(P).get(Q) == 0){
					zero = true;
				}else{
					um = true;
				}
			}
			
			if(!zero){
				cond3 = 0;
			}
			if(!um){
				cond2 = 0;
			}
		}

		result.add(cond1+cond2+cond3+cond4);		
	}

    public static void main(String[] args) {
    	Scanner scan = new Scanner(System.in);
		byte Pnum;
		int Qnum;

		while(true){
			Pnum = scan.nextByte();
			Qnum = scan.nextInt();
			
			if(Pnum == 0 && Qnum == 0){
				break;
			}
			
			List<List<Integer>> P = new ArrayList<List<Integer>>();
			
			//execuÃ§Ã£o

			for(byte x = 0; x < Pnum; x++){
				List<Integer> Q = new ArrayList<Integer>();
				for(int y = 0; y < Qnum; y++){
					Q.add(scan.nextInt());
				}
				P.add(Q);
			}

			resolver(P);

		}

		for(int x : result){
			System.out.println(x);
		}
    }
}