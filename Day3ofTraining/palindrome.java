package Day3ofTraining;

// ==========================================
// CONCEPT: String/Array Palindrome Checker
// ==========================================

public class palindrome {
    public static void main(String[] args) {
        
        String str[] = {"n","i","t","i","n"};
        int i;
        int j =  str.length-1;
        for(i=0;i<=j;i++){
            if(str[i]!=str[j]){
                System.out.println("String is not palindrome");
                break;
            }
            j--;
            if(i>=j){
                System.out.println("String is palindrome");
            }
            
        }

    }

}