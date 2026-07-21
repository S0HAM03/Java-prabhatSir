// ==========================================
// CONCEPT: Simple Inheritance & Object Creation
// ==========================================

// This is a "Base Class" or "Parent Class". 
// It contains properties and behaviors that other classes can inherit.
class Animal {
    public void eat() {
        System.out.println("The animal is eating...");
    }
}

// The 'extends' keyword creates an Inheritance relationship.
// 'Dog' is the "Child Class". It inherits the eat() method from Animal.
class Dog extends Animal {
    public void bark() {
        System.out.println("The dog is barking: Woof! Woof!");
    }
}

public class AnimalTest {
    // The main method is the entry point of any Java program.
    public static void main(String[] args) {
        System.out.println("--- Testing Dog and Animal Classes ---");
        
        // CONCEPT: Object Creation (Instantiation)
        // We are creating a new 'Dog' object named 'myDog'
        Dog myDog = new Dog();
        
        // myDog can use methods it inherited from the Animal class
        myDog.eat();
        
        // myDog can also use its own specific methods
        myDog.bark();
    }
}
