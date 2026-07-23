// ==========================================
// CONCEPT: Prime Number Checker Algorithm
// ==========================================
package Day3ofTraining;

public class primeNumbers {
    public static void main(String[] args){
        int num = 16;
        
        // IMPORTANT REMARK: Basic Prime Checking
        // This is a very simplified check. A true prime checking algorithm would loop 
        // from 2 up to the square root of 'num' and check if (num % i == 0).
        // This current logic only checks divisibility by 2 or 3, which works for small numbers,
        // but would falsely claim that 25 (divisible by 5) is Prime!
        if(num % 2 == 0 || num % 3 == 0){
            System.out.println("Number is composite");
        }
        else{
            System.out.println("Number is Prime");
        }    
    }
}