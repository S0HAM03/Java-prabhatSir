// ==========================================
// CONCEPT: Array Manipulation (Push Zeros to End)
// ==========================================
package Day5ofTraining;
import java.util.Arrays;

public class pushAll0slast {
    public static void main(String [] args){
        int[] arr = {7, 3, 0, 9, 0, 2, 0, 4, 4};
        
        // IMPORTANT REMARK: Two-Pointer Approach
        // 'i' keeps track of where the next NON-ZERO element should be placed.
        int i = 0; 
        
        // 'j' scans through the entire array.
        for (int j = 0; j < arr.length; j++) {
            // Whenever we find a non-zero element, swap it to position 'i'
            if (arr[j] != 0) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                
                i++; // Move the non-zero tracker forward
            }
        }
        
        System.out.println("After operations: " + Arrays.toString(arr));
    }
}