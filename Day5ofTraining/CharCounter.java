// ==========================================
// CONCEPT: HashMap (Counting Character Frequency)
// ==========================================
package Day5ofTraining;

import java.util.HashMap;

public class CharCounter {
    public static void main(String[] args) {
        Hasher("hello world");
    }
    
    public static void Hasher(String text) {
        // IMPORTANT REMARK: HashMaps store Key-Value pairs.
        // Here, the Key is the character, and the Value is how many times it appeared.
        HashMap<Character, Integer> counter = new HashMap<>();

        for(int i = 0; i < text.length(); i++){
            char currchar = text.charAt(i);
            
            // Check if the character is already in the map using containsKey()
            // (Previously this used .get() > 0, which crashes with a NullPointerException if it doesn't exist!)
            if(counter.containsKey(currchar)){
                // If yes, increment its count by 1
                counter.put(currchar, counter.get(currchar) + 1);
            } else {
                // If no, add it to the map with a count of 1
                counter.put(currchar, 1);
            }
        }
        
        System.out.println("Character frequencies: " + counter);
    }
}
