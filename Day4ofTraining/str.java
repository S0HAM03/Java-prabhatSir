// ==========================================
// CONCEPT: String Manipulation (Split & Length)
// ==========================================

public class str {
     public static void main(String[] args){
            String s = "Hello World";
            
            // IMPORTANT REMARK: Splitting Strings
            // The .split(" ") method breaks a string into a String Array based on the space character.
            // So "Hello World" becomes an array: ["Hello", "World"]
            String[] parts = s.split(" ");
            
            // To get the length of the LAST word, we access the very last element in the array
            // using parts[parts.length - 1], then call .length() on that specific String.
            System.out.println("Length of last word: " + parts[parts.length - 1].length());
    }
}
