import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
       Scanner in = new Scanner(System.in);
        
        String l1 = in.nextLine();
        String l2 = in.nextLine();
        
        String [] linha1 = l1.split(" ");
        String [] linha2 = l2.split(" ");
        
        int cod = Integer.parseInt(linha1[0]);
        int p = Integer.parseInt(linha1[1]);
        double valor = Double.parseDouble(linha1[2]);
        
        int cod2 = Integer.parseInt(linha2[0]);
        int p2 = Integer.parseInt(linha2[1]);
        double valor2 = Double.parseDouble(linha2[2]);
        
        double pagar1 = valor * p;
        double pagar2 = valor2 * p2;
        
        double res = pagar1 + pagar2;
        
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", res);
 
    }
 
}