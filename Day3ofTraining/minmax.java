// ==========================================
// CONCEPT: Array Min/Max Finding Algorithm
// ==========================================
package Day3ofTraining;

public class minmax {
    public static void main(String[] args){
        int[] arr = {1,34,23,0,-10};
        
        // IMPORTANT REMARK: Initialization
        // Always initialize min and max with the FIRST element of the array.
        // If you initialize with 0, it might fail if the array only has negative numbers!
        int min = arr[0];
        int max = arr[0];
        
        // Loop through the entire array
        for(int i=0;i<arr.length;i++){
            
            // If the current element is smaller than our known minimum, it becomes the new minimum.
            if(min > arr[i]){
                min = arr[i];
            }   
            
            // If the current element is larger than our known maximum, it becomes the new maximum.
            if(max < arr[i]){
                max = arr[i];
            }
        }
        
        System.out.println("Min: "+ min);
        System.out.println("Max: "+ max);
    }
}