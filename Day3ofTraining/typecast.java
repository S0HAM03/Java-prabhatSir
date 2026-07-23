// ==========================================
// CONCEPT: Primitive Typecasting
// ==========================================
package Day3ofTraining;

public class typecast {
     public static void main(String [] args){
        // Assigning a character to a float (implicit widening cast)
        float a1 = 'a';
        
        // Explicitly casting the float back into an integer
        // This will print out the ASCII numeric value for 'a', which is 97.
        int ascii = (int) a1;
        
        System.out.println("ASCII value is: "+ ascii);
    }
}