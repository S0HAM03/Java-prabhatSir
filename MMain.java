class Vehical{
    void start(){
        System.out.println("Yess is starting");
    }
}

class Car extends Vehical{
    void model(){
    System.out.println("Ferrari spider");
    }
}

class supercar extends Car{
    void speed(){
        System.out.println("Max Speed is 200 kph");
    }
}

public class MMain {
    public static void main(String[] args) {
        System.out.println("");
        
        supercar audi  = new supercar();
        
        audi.start();
        
        audi.model();

        audi.speed();
    }
}