import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner in = new Scanner(System.in);
        
        int a=in.nextInt();
        int b=in.nextInt();
        
        int c=in.nextInt();
        int d=in.nextInt();
        
        int dife = (a*b - c*d);
        
        String diff = String.format("DIFERENCA = %d", dife);
        
        System.out.println(diff);
 
    }
 
}