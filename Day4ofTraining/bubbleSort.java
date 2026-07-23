package Day4ofTraining;

// ==========================================
// CONCEPT: Sorting Algorithms - Bubble Sort
// ==========================================

import java.util.Arrays;

public class bubbleSort {
    public static void main(String[] args){
   int[] arr = {7,6,3,5,8,2,255,1};
    
     for(int i=0;i<arr.length-1;i++){
        boolean swapped = false;    
        for(int j=0; j<arr.length-i-1;j++){
        if(arr[j] > arr[j+1]){
            int temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
            swapped = true;
        }
    }
    if(!swapped){
        break;
    }

    }
        System.out.println("Sorted: "+ Arrays.toString(arr));
}
}