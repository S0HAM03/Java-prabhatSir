package Day2ofTraining;

// ==========================================
// CONCEPT: Multilevel Inheritance
// ==========================================

// Grandparent class
class Vehical{
    void start(){
        System.out.println("Yess is starting");
    }
}

// Parent class inherits from Grandparent
class Car extends Vehical{
    void model(){
        System.out.println("Ferrari spider");
    }
}

// Child class inherits from Parent
// Therefore, 'supercar' has access to methods from BOTH Car and Vehical!
class supercar extends Car{
    void speed(){
        System.out.println("Max Speed is 200 kph");
    }
}

public class MMain {
    public static void main(String[] args) {
        System.out.println("");
        
        // Creating the lowest-level child object
        supercar audi  = new supercar();
        
        // Inherited from Vehical (Grandparent)
        audi.start();
        
        // Inherited from Car (Parent)
        audi.model();

        // Specific to supercar (Child)
        audi.speed();
    }
}