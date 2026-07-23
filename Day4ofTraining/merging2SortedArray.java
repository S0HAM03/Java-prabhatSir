// ==========================================
// CONCEPT: Merging Two Sorted Arrays (Two Pointers)
// ==========================================
package Day4ofTraining;

import java.util.Arrays;

public class merging2SortedArray {
       public static void main(String[] args){
            // Two already sorted arrays
            int[] arr = {2,4,5,8,10};
            int[] arr1 = {3,4,7,9,12,56};
            
            int n = arr.length;
            int m = arr1.length;
            
            // Pointers for each array
            int i = 0; // Pointer for arr
            int j = 0; // Pointer for arr1
            int k = 0; // Pointer for the new merged array
            
            // The new array must hold all elements from both arrays
            int[] array = new int[n + m];

            // IMPORTANT REMARK: The Merge Process
            // Compare elements from both arrays. The smaller element gets added to the new array.
            while(i<n && j<m){
                if(arr[i] <= arr1[j]){
                    array[k] = arr[i];
                    i++;
                }
                else{
                    array[k] = arr1[j];
                    j++;
                }
                k++; // Move the pointer in the merged array forward
            }    
            
            // If arr1 ran out of elements, dump the rest of arr into the new array
            while(i<n){
                array[k] = arr[i];
                i++;
                k++;
            }
            
            // If arr ran out of elements, dump the rest of arr1 into the new array
            while(j<m){
                array[k] = arr1[j];
                j++;
                k++;
            }
            
            System.out.println(Arrays.toString(array));
        }
}