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

    def pay(self):
        print("Payment done using PhonePay")

    def check_balance(self):
        print("Balance checked using PhonePay")


class phonepayfinal(upi):

    def __init__(self):
        self.p = phonepay()

    def pay(self):
        return self.p.pay()

    def check_balance(self):
        return self.p.check_balance()


class googlepay:

    def make_payment(self):
        print("Payment done using GooglePay")

    def view_balance(self):
        print("Balance checked using GooglePay")


class googlepayfinal(upi):

    def __init__(self):
        self.g = googlepay()

    def pay(self):
        return self.g.make_payment()

    def check_balance(self):
        return self.g.view_balance()


class factory:

    def get_payment(self, payment_type):

        if payment_type == "phonepay":
            return phonepayfinal()

        elif payment_type == "googlepay":
            return googlepayfinal()

        else:
            return None


a = factory().get_payment("googlepay")

a.pay()
a.check_balance()
