// ==========================================
// CONCEPT: Interfaces and Multiple Inheritance
// ==========================================

// An Interface is like a contract. It only contains empty methods (no bodies).
// Any class that "implements" this interface MUST write the code for these methods.
interface Camera {
    void clickphoto();
}

interface Gps {
    void GpsService();
}

// Java does NOT support multiple inheritance with classes (you can't extend two classes).
// But you CAN implement multiple interfaces! This is how Java achieves multiple inheritance.
class Phone implements Camera, Gps{
    
    // @Override tells Java we are fulfilling the contract from the interface
    @Override
    public void clickphoto(){
        System.out.println("Take a photo");
    }

    @Override
    public void GpsService(){
        System.out.println("Click images with location");
    }
}

public class PracticeInterface {
    public static void main(String[] args) {
        Phone apple = new Phone();
        
        apple.clickphoto();
        apple.GpsService();
    }
}
