
class Employee{
    void working(){
         System.out.println("Working Class");
}
}
interface Hobby{
    void playing(){}
}

class Person extends Employee implements Hobby{
    void message(){
        System.out.println("This is person subclass");
    }
    @Override
     void playing(){
        System.out.println("Playing game");
     } 
}
public class Hybridinhetitance {
    public static void main(String[] args){
        Person man = new Person();
        man.playing();
        man.working();
    }   
}
