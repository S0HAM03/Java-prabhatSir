package Day3ofTraining;

public class numberPaindrome {
    public static void main(String[] args) { 

        int num=10001;
        int rem=0;
        int chk=0;
        int temp = num;

        while (temp != 0){
            rem = temp % 10;
            chk = (chk*10)+rem;
            temp = temp/10;
        }

        if(num == chk){
            System.out.println("Number is palindrome");
        }
        else{
            System.out.println("Number is not palindrome...");
        }
    }

}

