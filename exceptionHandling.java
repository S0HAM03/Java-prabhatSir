// ==========================================
// CONCEPT: Exception Handling & Scanner Input
// ==========================================

// Importing the Scanner class to read user input from the keyboard
import java.util.Scanner;

public class exceptionHandling {
    public static void main(String[] args){
        // Creating a Scanner object
        Scanner sc = new Scanner(System.in);
        
        int result = 0; 
        
        // A 'try' block contains code that might crash (throw an Exception)
        try{
            System.out.println("Enter a number: ");
            // Reading an integer from the user
            int num = sc.nextInt();
            
            // If the user enters '0', math cannot divide by zero!
            // This will instantly crash and throw an 'ArithmeticException'
            result = 100 / num;
            
        } catch (ArithmeticException e){
            // If the code in the 'try' block crashes with an ArithmeticException,
            // the program jumps here instead of completely crashing the app.
            System.out.println("ko - Cannot divide by zero!");
        }
        
        // Program continues safely because we "handled" the exception
        System.out.println("Output is : "+ result);
    }
}
