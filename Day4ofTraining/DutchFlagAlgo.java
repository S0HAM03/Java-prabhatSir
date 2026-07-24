// ==========================================
// CONCEPT: Dutch National Flag Algorithm (0s, 1s, 2s Sort)
// ==========================================
package Day4ofTraining;

import java.util.Arrays;

public class DutchFlagAlgo {
    public static void main(String[] args) {
        // Array containing only 0s, 1s, and 2s
        int[] arr = {2, 0, 2, 1, 1, 0, 1, 2, 0, 0};
        System.out.println("Original: " + Arrays.toString(arr));
        
        sortColors(arr);
        
        System.out.println("Sorted:   " + Arrays.toString(arr));
    }

    // IMPORTANT REMARK: Dutch National Flag Algorithm
    // Uses 3 pointers to sort an array of 0s, 1s, and 2s in a single pass O(N) time.
    public static void sortColors(int[] arr) {
        int low = 0;
        int mid = 0;
        int high = arr.length - 1;

        // Traverse the array
        while (mid <= high) {
            if (arr[mid] == 0) {
                // Swap arr[low] and arr[mid], move both forward
                int temp = arr[low];
                arr[low] = arr[mid];
                arr[mid] = temp;
                low++;
                mid++;
            } 
            else if (arr[mid] == 1) {
                // It's already in the correct middle section, just move mid forward
                mid++;
            } 
            else { // arr[mid] == 2
                // Swap arr[mid] and arr[high], move high backward
                int temp = arr[high];
                arr[high] = arr[mid];
                arr[mid] = temp;
                high--;
            }
        }
    }
}