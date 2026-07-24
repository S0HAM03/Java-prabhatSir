// ==========================================
// CONCEPT: Counting Repeated Elements
// ==========================================
package Day5ofTraining;

import java.util.HashMap;

public class countrepeated {
    
    public static void main(String[] args) {
        int[] arr = {10, 20, 10, 30, 20, 10, 40, 50, 40};
        countFrequencies(arr);
    }
    
    // IMPORTANT REMARK: Using HashMap to count occurrences
    // The key is the number, and the value is how many times it appeared.
    public static void countFrequencies(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // Loop through the array and populate the map
        for (int num : arr) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }
        
        // Print only the repeated elements
        System.out.println("Repeated Elements:");
        for (Integer key : map.keySet()) {
            if (map.get(key) > 1) {
                System.out.println(key + " occurs " + map.get(key) + " times");
            }
        }
    }
}
