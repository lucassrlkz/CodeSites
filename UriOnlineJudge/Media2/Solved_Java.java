import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
      Scanner in = new Scanner(System.in);
        
        double a=in.nextDouble();
        double b=in.nextDouble();
        double c=in.nextDouble();
        
        double media = ((a*2)+(b*3)+(c*5)) / (2+3+5);
        
        String med = String.format("MEDIA = %.1f", media);
        
        System.out.println(med);
 
    }
 
}