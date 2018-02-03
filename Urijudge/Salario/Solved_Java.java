import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner in = new Scanner(System.in);
        
        int n=in.nextInt();
        int h=in.nextInt();
        double sal=in.nextDouble();
        
        double sala = sal*h;
        
        System.out.printf("NUMBER = %d\n", n);
        
        String salario = String.format("SALARY = U$ %.2f", sala);
        
        System.out.println(salario);
 
    }
 
}