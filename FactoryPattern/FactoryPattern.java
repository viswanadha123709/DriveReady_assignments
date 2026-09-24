interface payment {
    void pay();
}

interface credit extends payment {
    void pay();
}

class sbi implements credit {
    public void pay() {
        System.out.println("Payment done through SBI");
    }
}

class hdfc implements credit {
    public void pay() {
        System.out.println("Payment done through HDFC");
    }
}

interface upi extends payment {
    void pay();
}

class paytm implements upi {
    public void pay() {
        System.out.println("Payment done through Paytm");
    }
}

class phonepe implements upi {
    public void pay() {
        System.out.println("Payment done through PhonePe");
    }
}

class factory {

    public static payment create(String method) {

        if (method.equals("sbi")) {
            return new sbi();
        }
        else if (method.equals("hdfc")) {
            return new hdfc();
        }
        else if (method.equals("paytm")) {
            return new paytm();
        }
        else if (method.equals("phonepe")) {
            return new phonepe();
        }
        else {
            return null;
        }
    }
}

class FactoryPattern {

    public static void main(String[] args) {

        payment s1 = factory.create("sbi");
        s1.pay();

        payment s2 = factory.create("phonepe");
        s2.pay();

        payment s3 = factory.create("hdfc");
        s3.pay();

        payment s4 = factory.create("paytm");
        s4.pay();
    }
}
