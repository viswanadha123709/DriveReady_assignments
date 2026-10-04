# Factory + Adapter Design Pattern

This project demonstrates how to combine the **Factory Pattern** and **Adapter Pattern** using both **Python** and **Java**.

The example uses payment systems such as **PhonePay** and **GooglePay**.

---

## Design Patterns Used

### 1. Adapter Pattern

The Adapter Pattern is used when an external class has a different interface from the interface expected by our application.

For example, our application expects:

```text
pay()
check_balance()
```

But an external payment system may provide:

```text
make_payment()
view_balance()
```

The Adapter converts the external interface into the interface expected by our application.

### 2. Factory Pattern

The Factory Pattern is responsible for creating the required payment object.

Instead of creating adapters directly:

```python
googlepay_adapter()
```

the client can ask the Factory:

```python
factory.get_payment("googlepay")
```

The Factory decides which object should be created.

---

# Overall Design

```text
                         Payment
                            |
                           UPI
                      /            \
                     /              \
                    ↓                ↓
           PhonePay Adapter    GooglePay Adapter
                  |                  |
                  ↓                  ↓
              PhonePay          GooglePay
```

The Factory is responsible for creating the appropriate Adapter.

```text
Client
   |
   ↓
Factory
   |
   ↓
Adapter
   |
   ↓
External Payment System
```

---

# Python Implementation

## Structure

```text
python/
│
├── payment.py
└── README.md
```

## Code

```python
from abc import ABC, abstractmethod


class payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class upi(payment):
    pass


class phonepay:

    def make_payment(self, amount):
        print("Payment made successfully using PhonePay of amount:", amount)

    def view_balance(self, balance):
        print("Current PhonePay balance:", balance)


class phonepay_adapter(upi):

    def pay(self):
        phonepay().make_payment(1000)

    def check_balance(self):
        phonepay().view_balance(5000)


class googlepay:

    def make_payment(self, amount):
        print("Payment made successfully using GooglePay of amount:", amount)

    def view_balance(self, balance):
        print("Current GooglePay balance:", balance)


class googlepay_adapter(upi):

    def pay(self):
        googlepay().make_payment(2000)

    def check_balance(self):
        googlepay().view_balance(8000)


class factory:

    def get_payment(self, payment_type):

        if payment_type == "phonepay":
            return phonepay_adapter()

        elif payment_type == "googlepay":
            return googlepay_adapter()

        return None


a = factory().get_payment("googlepay")

a.pay()
a.check_balance()
```

## Python Output

```text
Payment made successfully using GooglePay of amount: 2000
Current GooglePay balance: 8000
```

---

# Java Implementation

## Structure

```text
java/
│
└── Main.java
```

## Code

```java
interface payment {

    void pay();

    void check_balance();
}


class upi implements payment {

    @Override
    public void pay() {
    }

    @Override
    public void check_balance() {
    }
}


class phonepay {

    void make_payment(float amount) {
        System.out.println(
            "Payment made successfully using PhonePay of amount: " + amount
        );
    }

    void view_balance(float balance) {
        System.out.println(
            "Current PhonePay balance: " + balance
        );
    }
}


class phonepay_adapter extends upi {

    @Override
    public void pay() {
        new phonepay().make_payment(1000);
    }

    @Override
    public void check_balance() {
        new phonepay().view_balance(5000);
    }
}


class googlepay {

    void make_payment(float amount) {
        System.out.println(
            "Payment made successfully using GooglePay of amount: " + amount
        );
    }

    void view_balance(float balance) {
        System.out.println(
            "Current GooglePay balance: " + balance
        );
    }
}


class googlepay_adapter extends upi {

    @Override
    public void pay() {
        new googlepay().make_payment(2000);
    }

    @Override
    public void check_balance() {
        new googlepay().view_balance(8000);
    }
}


class factory {

    upi get_payment(String payment_type) {

        if (payment_type.equals("phonepay")) {
            return new phonepay_adapter();
        }

        else if (payment_type.equals("googlepay")) {
            return new googlepay_adapter();
        }

        return null;
    }
}


public class Main {

    public static void main(String[] args) {

        factory f = new factory();

        upi a = f.get_payment("googlepay");

        a.pay();
        a.check_balance();
    }
}
```

## Java Output

```text
Payment made successfully using GooglePay of amount: 2000.0
Current GooglePay balance: 8000.0
```

---

# Why Adapter Is Needed

Suppose our application expects:

```text
pay()
check_balance()
```

PhonePay provides:

```text
make_payment()
view_balance()
```

GooglePay also provides:

```text
make_payment()
view_balance()
```

The external classes don't follow our application's interface.

Therefore, we create adapters:

```text
phonepay_adapter
googlepay_adapter
```

The adapters translate:

```text
pay()
   ↓
make_payment()

check_balance()
   ↓
view_balance()
```

The client does not need to know the external API.

---

# Why Factory Is Needed

Without Factory:

```python
a = googlepay_adapter()
```

The client needs to know the exact class.

With Factory:

```python
a = factory().get_payment("googlepay")
```

The client only provides the payment type.

The Factory handles object creation.

---

# Benefits

* Separates client code from external payment systems.
* Allows different payment providers to follow a common interface.
* Makes it easier to integrate third-party APIs.
* Factory hides object creation.
* Adapter hides differences between external APIs.
* Supports polymorphism.
* The same design can be extended to additional payment providers.

---

# Future Extension

The design can later be extended to support **Card Payments**.

For example:

```text
Payment
│
├── UPI
│   ├── PhonePay Adapter
│   └── GooglePay Adapter
│
└── Card
    ├── Visa Adapter
    └── MasterCard Adapter
```

The Factory can then create the required payment implementation.

---

# Design Principle

The main idea of this project is:

```text
Client
   ↓
Factory
   ↓
Common Interface
   ↓
Adapter
   ↓
External System
```

The **Factory decides what object to create**, while the **Adapter makes incompatible interfaces work together**.

---

## Technologies

* Python
* Java
* Object-Oriented Programming
* Factory Design Pattern
* Adapter Design Pattern
* Abstraction
* Polymorphism
* Composition
