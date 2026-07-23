// ==========================================
// CONCEPT: String/Array Palindrome Checker (Two Pointers)
// ==========================================
package Day3ofTraining;

public class palindrome {
    public static void main(String[] args) {
        
        String str[] = {"n","i","t","i","n"};
        
        // IMPORTANT REMARK: Two-Pointer Technique
        // 'i' starts at the beginning (left pointer)
        // 'j' starts at the very end (right pointer)
        int i;
        int j =  str.length-1;
        
        for(i=0;i<=j;i++){
            // If the character on the left doesn't match the character on the right, it fails immediately.
            if(str[i]!=str[j]){
                System.out.println("String is not palindrome");
                break;
            }
            // Move the right pointer inwards
            j--;
            
            // If the pointers have crossed (i >= j), we successfully checked the whole array!
            if(i>=j){
                System.out.println("String is palindrome");
            }
        }
    }
}