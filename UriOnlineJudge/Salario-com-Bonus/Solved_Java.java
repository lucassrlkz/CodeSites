import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner in = new Scanner(System.in);
        
        String nome = in.next();
        double sal = in.nextDouble();
        double vendas = in.nextDouble();
        
        double comissao = (vendas*0.15);
        
        sal = sal + comissao;
        
        String res = String.format("TOTAL = R$ %.2f", sal);
        
        System.out.println(res);
 
    }
 
}