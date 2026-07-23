// ==========================================
// CONCEPT: String Manipulation (Split & Length)
// ==========================================

public class str {
     public static void main(String[] args){
            String s = "Hello World";
            String[] parts = s.split(" ");
            System.out.println("Length of last word: " + parts[parts.length - 1].length());
    }
}
