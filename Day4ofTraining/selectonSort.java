// ==========================================
// CONCEPT: Sorting Algorithms - Selection Sort
// ==========================================
package Day4ofTraining;

import java.util.Arrays;

public class selectonSort {
    public static void main(String[] args){
        int[] arr = {7,6,3,5,8,2,255,1,45,3,7};
    
        // IMPORTANT REMARK: Selection Sort Logic
        // Selection sort divides the array into a sorted and an unsorted region.
        // It repeatedly selects the smallest (or largest) element from the unsorted region 
        // and swaps it to the front.
        
        // The outer loop tracks the boundary of the sorted region
        for(int i=0; i<=arr.length-1; i++){
            
            // The inner loop scans the unsorted region
            for(int j=i+1; j<arr.length; j++){
                
                // If it finds a smaller element than the boundary element, they are swapped!
                if(arr[i] >= arr[j]){
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        
        System.out.println("Sorted: "+ Arrays.toString(arr));
    }
}