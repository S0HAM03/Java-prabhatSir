// ==========================================
// CONCEPT: Array Reversing Algorithm (Two Pointers)
// ==========================================
package Day3ofTraining;

public class ReverseArray {
    public static void main(String[] args){
        int[] arr = {1,2,3};
        
        // IMPORTANT REMARK: Two-Pointer Technique
        // We use two pointers to swap elements from the outside in.
        int i = 0; // Pointer starting at the front
        int j = arr.length-1; // Pointer starting at the back
        int temp = 0; 
        
        System.out.println("Swapped array: ");
        
        // The loop continues as long as the front pointer hasn't crossed the back pointer.
        // Wait, the logic here actually prints the swapped values as it goes!
        for( i = 0; i<=j ;i++){
             // Swap logic using a temporary variable
             temp = arr[i];
             arr[i] = arr[j];
             arr[j] = temp;   
             
             // Move the back pointer inward (the front pointer 'i' is moved by the for-loop)
             j--;
             System.out.println(arr[i]);
        }
    }
}