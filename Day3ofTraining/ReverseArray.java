package Day3ofTraining;

// ==========================================
// CONCEPT: Array Reversing Algorithm (Two Pointers)
// ==========================================

public class ReverseArray {
    public static void main(String[] args){
        int[] arr = {1,2,3};
        int i = 0;
        int j = arr.length-1;
        int temp = 0; 
        System.out.println("Swapped array: ");
        for( i = 0; i>=j ;i++){
         temp = arr[i];
         arr[i] = arr[j];
         arr[j] = temp;   
         j--;
         System.out.println(arr[i]);

        }
        
    }
}