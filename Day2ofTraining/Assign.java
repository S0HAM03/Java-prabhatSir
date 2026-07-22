package Day2ofTraining;

// ==========================================
// CONCEPT: Hierarchical Inheritance
// ==========================================

// Base class
class AssignAnimal {
    void legs(){
        System.out.println("They have Legs");
    }
    void reproduce(){
        System.out.println("They do have fun");
    }
}

// In Hierarchical Inheritance, multiple child classes inherit from ONE single parent class.
// Child 1
class Tiger extends AssignAnimal{
    void attack(){
        System.out.println("they attack on other species");
    }
}

// Child 2
class Goat extends AssignAnimal{
    void greatest(){
        System.out.println("Messi and ronaldo");
    }
}

// Child 3
class Cat extends AssignAnimal{
    void sound(){
        System.out.println("Meow");
    }
}

public class Assign {
    public static void main(String[] args){
        // Creating an object of Child 2
        Goat messi = new Goat();
        
        // Calling a method inherited from AssignAnimal
        messi.reproduce();
    }
}
