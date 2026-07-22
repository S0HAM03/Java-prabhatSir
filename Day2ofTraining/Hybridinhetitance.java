package Day2ofTraining;

// ==========================================
// CONCEPT: Hybrid Inheritance
// ==========================================

class Employee{
    void working(){
         System.out.println("Working Class");
    }
}

interface Hobby{
    void playing(); // Interface methods cannot have a body
}

// Hybrid Inheritance means combining standard class inheritance (extends)
// with interface implementation (implements) on the same class!
class Person extends Employee implements Hobby{
    void message(){
        System.out.println("This is person subclass");
    }
    
    // Fulfilling the Hobby interface contract
    @Override
    public void playing(){ 
        System.out.println("Playing game");
    } 
}

public class Hybridinhetitance {
    public static void main(String[] args){
        Person man = new Person();
        
        // Method from interface
        man.playing();
        
        // Method inherited from Employee class
        man.working();
    }   
}
