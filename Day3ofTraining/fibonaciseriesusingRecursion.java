package Day3ofTraining;

public class fibonaciseriesusingRecursion {
    public static void main(String[] args){
        int x,y,z;
        x = 0;
        y = 1;
        z = 0;
        int n = 10;
        System.out.println("Fibonacci: "+ x + y);
        for(int i = 0; i <= n; i++){
            z = x + y;
            x = y;
            y = z;
            System.out.println(z);
        }
    }
}

