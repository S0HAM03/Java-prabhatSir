package Day4ofTraining;

// ==========================================
// CONCEPT: Merging Two Sorted Arrays (Two Pointers)
// ==========================================

import java.util.Arrays;

public class merging2SortedArray {
       public static void main(String[] args){
            int[] arr = {2,4,5,8,10};
            int[] arr1 = {3,4,7,9,12,56};
            int n = arr.length;
            int m = arr1.length;
            int i=0;
            int j=0;
            int k=0;
            int[] array = new int[n + m];

            while(i<n && j<m){
                if(arr[i] <= arr1[j]){
                    array[k] = arr[i];
                     i++;
                }
                else{
                    array[k] = arr1[j];
                    j++;
                }
                k++;
            }    
            while(i<n){
                array[k] = arr[i];
                     i++;
                     k++;
            }
            while(j<m){
                array[k] = arr1[j];
                    j++;
                    k++;
            }
            System.out.println(Arrays.toString(array));
            }
            
        
               
}