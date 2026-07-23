package Day3ofTraining;

// ==========================================
// CONCEPT: Array Min/Max Finding Algorithm
// ==========================================

public class minmax {
    public static void main(String[] args){
        int[] arr = {1,34,23,0,-10};
        int min = arr[0];
        int max = arr[0];
        for(int i=0;i<arr.length;i++){
            if(min > arr[i]){
                min = arr[i];
            }   
            if(max < arr[i]){
                max = arr[i];
            }
        }
        System.out.println("Min: "+ min);
        System.out.println("Max: "+ max);
    }
}