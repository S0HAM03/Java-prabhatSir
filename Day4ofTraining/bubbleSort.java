// ==========================================
// CONCEPT: Sorting Algorithms - Bubble Sort
// ==========================================
package Day4ofTraining;

import java.util.Arrays;

public class bubbleSort {
    public static void main(String[] args){
        int[] arr = {7,6,3,5,8,2,255,1};
        
        // IMPORTANT REMARK: Bubble Sort Logic
        // Bubble Sort repeatedly steps through the list, compares adjacent elements,
        // and swaps them if they are in the wrong order. 
        // The pass through the list is repeated until the list is sorted.
        
        // The outer loop keeps track of passes. We need at most (length - 1) passes.
        for(int i=0; i<arr.length-1; i++){
            boolean swapped = false;    
            
            // The inner loop pushes the largest remaining element to the end of the array.
            // Notice we do (arr.length - i - 1) because the last 'i' elements are already sorted!
            for(int j=0; j<arr.length-i-1; j++){
                
                // Compare adjacent elements
                if(arr[j] > arr[j+1]){
                    // Swap them if the left one is larger
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = true;
                }
            }
            
            // Optimization: If no elements were swapped in the inner loop, the array is fully sorted early!
            if(!swapped){
                break;
            }
        }
        
        System.out.println("Sorted: "+ Arrays.toString(arr));
    }
}