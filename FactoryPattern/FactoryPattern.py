from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class Credit(Payment):

    @abstractmethod
    def pay(self):
        pass


class SBI(Credit):

    def pay(self):
        print("Payment done through SBI")


class HDFC(Credit):

    def pay(self):
        print("Payment done through HDFC")


class UPI(Payment):

    @abstractmethod
    def pay(self):
        pass


class Paytm(UPI):

    def pay(self):
        print("Payment done through Paytm")


class PhonePe(UPI):

    def pay(self):
        print("Payment done through PhonePe")


class PaymentFactory:

    @staticmethod
    def create(method):

        if method == "sbi":
            return SBI()

        elif method == "hdfc":
            return HDFC()

        elif method == "paytm":
            return Paytm()

        elif method == "phonepe":
            return PhonePe()

        else:
            return None


class Main:

    @staticmethod
    def main():

        s1 = PaymentFactory.create("sbi")
        s1.pay()

        s2 = PaymentFactory.create("phonepe")
        s2.pay()


if __name__ == "__main__":
    Main.main()
