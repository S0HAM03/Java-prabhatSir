class Animal {
    void legs(){
        System.out.println("They have Legs");
    }
    void reproduce(){
        System.out.println("They do have fun");
    }
}

class Tiger extends Animal{
    void attack(){
        System.out.println("they attack on other species");
    }
}

class Goat extends Animal{
    void Grestest(){
        System.out.println("Messi and ronaldo");
    }
}

class donkey extends Animal{
    void faculty(){
        System.out.println("IYKYK");
    }
}

public class assign {
    public static void main(String[] args){
        Goat messi = new Goat();
        messi.reproduce();
    }
}
