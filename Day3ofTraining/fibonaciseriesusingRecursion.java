// ==========================================
// CONCEPT: Fibonacci Series (Notice: This is Iterative!)
// ==========================================
package Day3ofTraining;

public class fibonaciseriesusingRecursion {
    public static void main(String[] args){
        int x,y,z;
        x = 0;
        y = 1;
        z = 0;
        int n = 10;
        
        // IMPORTANT REMARK: Recursion vs Iteration
        // Although this file is named "usingRecursion", the code here is actually using a standard 
        // iterative 'for' loop. A true recursive approach would involve the function calling itself!
        System.out.println("Fibonacci: "+ x + y);
        for(int i = 0; i <= n; i++){
            z = x + y;
            x = y;
            y = z;
            System.out.println(z);
        }
    }
}