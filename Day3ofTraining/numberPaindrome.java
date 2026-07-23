// ==========================================
// CONCEPT: Number Palindrome Checker
// ==========================================
package Day3ofTraining;

public class numberPaindrome {
    public static void main(String[] args) { 

        int num=10001;
        int rem=0;
        int chk=0; // This will store our reversed number
        
        // We use a temporary variable because we will destroy 'temp' during the loop, 
        // and we need 'num' intact to compare at the very end.
        int temp = num;

        // IMPORTANT REMARK: Reversing an Integer
        // This loop extracts digits from right-to-left and builds a reversed integer.
        while (temp != 0){
            // 1. Get the last digit (e.g. 10001 % 10 = 1)
            rem = temp % 10;
            
            // 2. Shift the current reversed number left by multiplying by 10, then add the new digit.
            chk = (chk*10)+rem;
            
            // 3. Remove the last digit from the temp number
            temp = temp/10;
        }

        // If the original number is equal to the reversed number, it's a palindrome!
        if(num == chk){
            System.out.println("Number is palindrome");
        }
        else{
            System.out.println("Number is not palindrome...");
        }
    }

}