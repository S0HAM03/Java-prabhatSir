# Java by Prabhat Sir ☕

Welcome to the **Java by Prabhat Sir** repository! 
This project is a beginner-friendly collection of Java exercises designed to teach and demonstrate fundamental Object-Oriented Programming (OOP) concepts. Every file in this repository has been carefully documented with educational comments to help new Java developers understand exactly how the code works under the hood.

---

## 📚 What this Repository Contains

This repository is packed with bite-sized, runnable Java files that each demonstrate a specific OOP or core Java concept:

- **`AnimalTest.java`**: Demonstrates **Simple Inheritance** and Object Creation. Contains a base class and a `Dog` subclass.
- **`Assign.java`**: Demonstrates **Hierarchical Inheritance**, where multiple classes (`Tiger`, `Goat`, `Cat`, `Donkey`) inherit from a single `AssignAnimal` base class.
- **`MMain.java`**: Demonstrates **Multilevel Inheritance**. Shows how a child class (`supercar`) inherits from a parent (`Car`), which inherits from a grandparent (`Vehical`).
- **`PracticeInterface.java`**: Demonstrates **Interfaces and Multiple Inheritance**. Shows how Java uses interfaces (`Camera`, `Gps`) to allow a class (`Phone`) to inherit multiple behaviors.
- **`Hybridinhetitance.java`**: Demonstrates **Hybrid Inheritance**. A class (`Person`) extends another class (`Employee`) while simultaneously implementing an interface (`Hobby`).
- **`exceptionHandling.java`**: Demonstrates basic **Exception Handling** using `try-catch` blocks to catch an `ArithmeticException` (division by zero), and reading user input using the `Scanner` class.

---

## 🚀 How to Clone and Run Locally

If you want to download this code to your own computer and run it, follow these simple steps!

### Prerequisites
You must have the **Java Development Kit (JDK)** installed on your machine. You can download it from [Adoptium](https://adoptium.net/) or Microsoft.

### 1. Clone the Repository
Open your terminal or command prompt and run the following command to download the code to your machine:
```bash
git clone https://github.com/S0HAM03/Java-prabhatSir.git
```

### 2. Navigate to the Folder
Move into the project directory you just cloned:
```bash
cd Java-prabhatSir
```

### 3. Compile the Code
Before running a Java file, you must compile it into bytecode (`.class` files) using the `javac` compiler. Pick the file you want to run (for example, `AnimalTest.java`):
```bash
javac AnimalTest.java
```

### 4. Run the Code
Once compiled, run the bytecode using the `java` command. **Do not include the `.java` extension here!**
```bash
java AnimalTest
```

*(You can repeat steps 3 and 4 for any of the `.java` files in this repository!)*
