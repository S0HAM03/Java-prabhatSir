import java.util.Scanner;

public class exceptionHandling {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        try{

        // System.out.println("Enter a number: ");
        int num = sc.nextInt();
        int result = 100/num;
        }catch (ArithmeticException e){
                System.out.println("ko");
        }
        // System.out.println("Output is : "+ result);
    }
}

