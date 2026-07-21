class Animal {
    public void eat() {
        System.out.println("The animal is eating...");
    }
}

class Dog extends Animal {
    public void bark() {
        System.out.println("The dog is barking: Woof! Woof!");
    }
}

public class Animal {
    public static void main(String[] args) {
        System.out.println("--- Testing Dog and Animal Classes ---");
        
        Dog myDog = new Dog();
        
        myDog.eat();
        
        myDog.bark();
    }
}
