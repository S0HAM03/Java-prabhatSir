// ==========================================
// CONCEPT: Typecasting (char to int)
// ==========================================
package Day3ofTraining;

public class ASCICON {
    public static void main(String [] args){
        // A 'char' stores a single character in single quotes.
        char a1 = 'a';
        
        // IMPORTANT REMARK: Typecasting
        // We are forcing Java to convert the character 'a' into an integer.
        // This reveals its underlying ASCII numeric value (which is 97 for 'a').
        int ascii = (int) a1;
        
        System.out.println("ASCII value is: "+ ascii);
    }
}