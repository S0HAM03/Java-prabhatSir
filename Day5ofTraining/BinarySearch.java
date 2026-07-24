// ==========================================
// CONCEPT: Binary Search Algorithm
// ==========================================
package Day5ofTraining;

public class BinarySearch {
    public static void main(String [] args){
        // IMPORTANT REMARK: Binary Search requires a SORTED array!
        int[] arr={2,3,4,6,8,9,12,15,16};
        int low = 0;
        int high = arr.length-1;
        int target = 1; // Searching for 1 (which is not in the array)
        boolean found = false;

        // Loop until the search space is exhausted
        while(low <= high){
            // Calculate the middle index (avoids overflow compared to (low+high)/2)
            int mid = low + (high-low)/2;

            if(arr[mid] == target){
                System.out.println("Found at index: " + mid);
                found = true;
                break;
            }
            else if(arr[mid] < target){
                // Target is in the right half, discard the left half
                low = mid + 1;
            }
            else {
                // Target is in the left half, discard the right half
                high = mid - 1;
            }
        } 
        
        // Check if we found the element after the loop finishes
        if(!found){
            System.out.println("Element not found");
        }
    }   
}
