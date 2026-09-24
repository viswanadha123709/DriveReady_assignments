# 💳 Payment Factory – Java

A simple Java project demonstrating how **interfaces, interface inheritance, polymorphism, and the Factory Design Pattern** can be used to create different payment implementations.

## 📌 Overview

This project defines a common `Payment` interface and multiple payment methods such as:

* SBI
* HDFC
* Paytm
* PhonePe

The `PaymentFactory` class is responsible for creating the appropriate payment object based on the method provided.

Instead of directly creating objects like:

```java
SBI sbi = new SBI();
PhonePe phonePe = new PhonePe();
```

the client uses the factory:

```java
Payment payment = PaymentFactory.create("sbi");
payment.pay();
```

This keeps object creation centralized and allows the client code to depend on the `Payment` interface.

---

## 🏗️ Project Structure

```text
Payment Factory
│
├── Payment
│   └── pay()
│
├── Credit extends Payment
│   ├── SBI implements Credit
│   └── HDFC implements Credit
│
├── UPI extends Payment
│   ├── Paytm implements UPI
│   └── PhonePe implements UPI
│
└── PaymentFactory
    └── create(method)
```

### Class Relationship

```text
                 Payment
                /       \
               /         \
          Credit          UPI
          /   \          /   \
        SBI   HDFC    Paytm  PhonePe
```

---

## 🔑 Concepts Demonstrated

### 1. Interface

`Payment` defines the common contract:

```java
interface Payment {
    void pay();
}
```

Every payment implementation must provide the `pay()` method.

---

### 2. Interface Inheritance

`Credit` and `UPI` extend the `Payment` interface:

```java
interface Credit extends Payment {
    void pay();
}

interface UPI extends Payment {
    void pay();
}
```

This demonstrates that **one interface can extend another interface**.

---

### 3. Polymorphism

The factory returns a `Payment` reference:

```java
Payment payment = PaymentFactory.create("sbi");
payment.pay();
```

The actual object can be `SBI`, `HDFC`, `Paytm`, or `PhonePe`.

```text
Payment reference
       ↓
 ┌─────┼─────┬─────┐
 ↓     ↓     ↓     ↓
SBI  HDFC  Paytm PhonePe
```

The correct `pay()` implementation is executed at runtime.

---

### 4. Factory Design Pattern

The `PaymentFactory` handles object creation:

```java
class PaymentFactory {

    public static Payment create(String method) {

        if (method.equals("sbi")) {
            return new SBI();
        }
        else if (method.equals("hdfc")) {
            return new HDFC();
        }
        else if (method.equals("paytm")) {
            return new Paytm();
        }
        else if (method.equals("phonepe")) {
            return new PhonePe();
        }

        return null;
    }
}
```

The client does not need to know which concrete class needs to be instantiated.

---

## 🚀 Example

```java
public class Main {

    public static void main(String[] args) {

        Payment p1 = PaymentFactory.create("sbi");
        p1.pay();

        Payment p2 = PaymentFactory.create("phonepe");
        p2.pay();
    }
}
```

### Output

```text
Payment done through SBI
Payment done through PhonePe
```

---

## 💡 Why Use Factory Pattern?

Without a factory:

```java
Payment p1 = new SBI();
Payment p2 = new HDFC();
Payment p3 = new Paytm();
Payment p4 = new PhonePe();
```

The client directly depends on concrete classes.

With a factory:

```java
Payment p1 = PaymentFactory.create("sbi");
Payment p2 = PaymentFactory.create("phonepe");
```

Object creation is centralized in one place.

### Benefits

* Centralizes object creation
* Reduces direct dependency on concrete classes
* Makes the code easier to extend
* Demonstrates polymorphism
* Improves separation of responsibilities

---

## 🛠️ Technologies

* **Java**
* **Interfaces**
* **Interface Inheritance**
* **Runtime Polymorphism**
* **Factory Design Pattern**

---

## ▶️ How to Run

### 1. Compile

```bash
javac Main.java
```

### 2. Run

```bash
java Main
```

---

## 📚 Learning Outcome

This project helps understand the relationship between:

```text
Interface
    ↓
Interface Inheritance
    ↓
Implementation Classes
    ↓
Polymorphism
    ↓
Factory Pattern
```

It is a beginner-friendly example of applying **object-oriented programming and design patterns in Java**.
