// ==========================================
// CONCEPT: Parameterized Constructors & Object Instantiation
// ==========================================
package Day3ofTraining;

public class parameterizedConstructor {
    public static void main(String[] args){
        // In a real application, you would instantiate the Student object here
        // Example: Student s1 = new Student("Soham", 1, "2026", "CS", 9.5f);
    }
}

class Student{
    // Class properties (Attributes)
    String name;
    int Rno;
    String year;
    String depa;
    float CGPA;

    // IMPORTANT REMARK: Parameterized Constructor
    // A constructor is a special method that runs the moment you use 'new Student(...)'.
    // A "Parameterized" constructor accepts arguments so you can initialize the object's properties immediately!
    Student(String sname, int sRno, String syear, String sdepa, float sCGPA ){
        this.CGPA = sCGPA;
        this.name = sname;
        this.Rno = sRno;
        this.depa = sdepa;
        this.year = syear;
    }
}