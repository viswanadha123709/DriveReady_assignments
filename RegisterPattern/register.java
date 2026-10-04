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
        System.out.println("Payment made successfully using PhonePay of amount: " + amount);
    }

    void view_balance(float balance) {
        System.out.println("Current PhonePay balance: " + balance);
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
        System.out.println("Payment made successfully using GooglePay of amount: " + amount);
    }

    void view_balance(float balance) {
        System.out.println("Current GooglePay balance: " + balance);
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

class factory{
    
    public static upi getInstance(String type) {
        if (type.equalsIgnoreCase("phonepay")) {
            return new phonepay_adapter();
        } else if (type.equalsIgnoreCase("googlepay")) {
            return new googlepay_adapter();
        }
        return null;
    }
}
class Main {

    public static void main(String[] args) {

        payment a = factory.getInstance("phonepay");
        a.pay();
        a.check_balance();

        System.out.println();

        payment b = factory.getInstance("googlepay");
        b.pay();
        b.check_balance();
    }
}
