package Day3ofTraining;

// ==========================================
// CONCEPT: Variable Swapping (Without 3rd Variable)
// ==========================================

public class swap {
    public static void main(String [] args){
        int var1 = 10;
        int var2 = 20;
        var1 = var1 + var2;
        var2 = var1 - var2;
        var1 = var1 - var2;
        System.out.println("Variable 1:"+var1);
        System.out.println("Variable 2:"+var2);
    }
}