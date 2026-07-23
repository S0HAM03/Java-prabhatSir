package Day3ofTraining;

// ==========================================
// CONCEPT: Parameterized Constructors & Object Instantiation
// ==========================================

public class parameterizedConstructor {
    public static void main(String[] args){

    }
}

class Student{
    String name;
    int Rno;
    String year;
    String depa;
    float CGPA;

    Student(String sname, int sRno, String syear, String sdepa, float sCGPA ){
        this.CGPA = sCGPA;
        this.name = sname;
        this.Rno = sRno;
        this.depa = sdepa;
        this.year = syear;
    }

    
}