// ==========================================
// CONCEPT: Variable Swapping (Without 3rd Variable)
// ==========================================
package Day3ofTraining;

public class swap {
    public static void main(String [] args){
        int var1 = 10;
        int var2 = 20;
        
        // IMPORTANT REMARK: Mathematical Swap
        // Usually, swapping requires a 3rd 'temp' variable. 
        // But you can swap two numbers using just math (addition and subtraction)!
        
        // Step 1: var1 becomes the total sum (10 + 20 = 30)
        var1 = var1 + var2;
        
        // Step 2: var2 becomes the total minus its own value (30 - 20 = 10). var2 is now 10!
        var2 = var1 - var2;
        
        // Step 3: var1 becomes the total minus the NEW var2 (30 - 10 = 20). var1 is now 20!
        var1 = var1 - var2;
        
        System.out.println("Variable 1:"+var1);
        System.out.println("Variable 2:"+var2);
    }
}