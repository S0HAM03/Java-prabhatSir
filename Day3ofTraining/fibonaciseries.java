// ==========================================
// CONCEPT: Fibonacci Series (Iterative Approach)
// ==========================================
package Day3ofTraining;

public class fibonaciseries {
    public static void main(String[] args){
        // Variables to store the current, next, and sum of numbers
        int x,y,z;
        x = 0; // First number of Fibonacci
        y = 1; // Second number of Fibonacci
        z = 0; 
        
        int n = 10; // Number of iterations
        System.out.println("Fibonacci: "+ x + y);
        
        // IMPORTANT REMARK: The Loop Logic
        // In a Fibonacci sequence, the next number is always the sum of the previous two.
        for(int i = 0; i <= n; i++){
            // 1. Calculate the next number
            z = x + y;
            
            // 2. Shift the variables forward for the next loop
            x = y;
            y = z;
            
            // 3. Print the newly generated number
            System.out.println(z);
        }
    }
}