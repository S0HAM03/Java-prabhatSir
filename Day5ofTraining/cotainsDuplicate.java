// ==========================================
// CONCEPT: Hashing (Finding Duplicates)
// ==========================================
package Day5ofTraining;

import java.util.HashSet;

public class cotainsDuplicate {
    public static void main(String[] args) {
        int[] arr = {6, 6};
        
        // IMPORTANT REMARK: Type Matching
        // The contain() method returns a boolean, so we must store it in a boolean variable!
        // (Previously it tried to store a boolean in a String, causing a crash)
        boolean ans = contain(arr);
        System.out.println("Contains duplicate? " + ans);
    }

    public static boolean contain(int[] arr){
        // A HashSet only stores UNIQUE values. 
        HashSet<Integer> hasharr = new HashSet<>();

        // Loop through every number in the array
        for(int num : arr){
            // If the set already contains the number, we found a duplicate!
            if(hasharr.contains(num)){
                return true;
            } else {
                // Otherwise, add it to the set and keep checking
                hasharr.add(num);
            }
        }
        return false;
    }    
}